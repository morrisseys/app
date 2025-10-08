from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware
from routers import reporting

app = FastAPI(title="RMY (UK)")

# Security headers for same-origin iframe
class SecurityHeaders(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        resp = await call_next(request)
        resp.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
        resp.headers.setdefault("Content-Security-Policy", "frame-ancestors 'self'; frame-src 'self';")
        return resp

app.add_middleware(SecurityHeaders)

# Static & templates
app.mount("/static", StaticFiles(directory="static"), name="static")
app.state.templates = Jinja2Templates(directory="templates")

# Routers
app.include_router(reporting.router)

@app.get("/health")
async def health():
    return {"ok": True}
