from fastapi import FastAPI
from .routers import org, admin

app = FastAPI(title="Organization Management Service")
app.include_router(org.router)
app.include_router(admin.router)

@app.get("/health")
async def health():
    return {"status": "ok"}