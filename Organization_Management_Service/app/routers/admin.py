from fastapi import APIRouter, HTTPException
from ..schemas import AdminLogin
from ..crud import admin_login

router = APIRouter()

@router.post("/admin/login")
async def login(payload: AdminLogin):
    res = await admin_login(payload.email, payload.password)
    if not res:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return res