from fastapi import APIRouter, Request, Response, Depends, HTTPException
from starlette.responses import HTMLResponse
import httpx

router = APIRouter()
DASH_BASE = "http://dashboards:5601/_reporting"

# Dummy auth; replace with real RBAC
class DummyUser:
    def __init__(self):
        self.global_id = 1
        self.can_report = True
        self.reporting_roles = ["rmy-tenant-example"]

async def require_reporting_access(request: Request):
    user = DummyUser()
    if not user.can_report:
        raise HTTPException(403, "Reporting not permitted")
    request.state.user = user
    return user

@router.get("/t/{tenant}/reporting", response_class=HTMLResponse)
async def reporting_home(tenant: str, request: Request, user=Depends(require_reporting_access)):
    target_path = "app/home"
    return request.app.state.templates.TemplateResponse(
        "reporting.html",
        {"request": request, "tenant": tenant, "iframe_src": f"/_reporting/{target_path}", "title": "Reporting"},
    )

@router.api_route("/_reporting/{path:path}", methods=["GET","POST","PUT","PATCH","DELETE","HEAD","OPTIONS"])
async def reporting_proxy(path: str, request: Request, user=Depends(require_reporting_access)):
    headers = {k: v for k, v in request.headers.items() if k.lower() not in {
        "host","connection","keep-alive","proxy-authenticate","proxy-authorization","te","trailers","transfer-encoding","upgrade"
    }}
    headers["x-proxy-user"] = f"user-{user.global_id}"
    headers["x-proxy-roles"] = ",".join(user.reporting_roles)
    upstream = f"{DASH_BASE}/{path}"
    async with httpx.AsyncClient(follow_redirects=False) as client:
        body = await request.body()
        resp = await client.request(request.method, upstream, headers=headers, content=body)
    excluded = {"content-encoding","transfer-encoding","connection"}
    filtered = {k: v for k, v in resp.headers.items() if k.lower() not in excluded}
    return Response(content=resp.content, status_code=resp.status_code, headers=filtered)
