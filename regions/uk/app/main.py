from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from routers import reporting

app = FastAPI(title="RMY (UK) — AdminLTE")

class SecurityHeaders(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        resp = await call_next(request)
        resp.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        resp.headers.setdefault("Content-Security-Policy", "frame-ancestors 'self'; frame-src 'self';")
        return resp

app.add_middleware(SecurityHeaders)

from starlette.middleware.base import BaseHTTPMiddleware

class ForwardedProtoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        xf_proto = request.headers.get("x-forwarded-proto")
        if xf_proto:
            request.scope["scheme"] = xf_proto  # make url_for use https
        return await call_next(request)

app.add_middleware(ForwardedProtoMiddleware)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.state.templates = templates

app.include_router(reporting.router)

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tenant": "example", "title": "Home"})

@app.get("/health")
async def health():
    return {"ok": True}
