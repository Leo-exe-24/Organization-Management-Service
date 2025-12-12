from fastapi import APIRouter, HTTPException, Depends
from ..schemas import OrgCreate, OrgOut
from ..crud import create_organization, get_organization, update_organization, delete_organization
from ..auth import get_current_admin

router = APIRouter()

@router.post("/org/create")
async def create_org(payload: OrgCreate):
    res = await create_organization(payload.organization_name, payload.email, payload.password)
    if isinstance(res, dict) and res.get("error") == "organization_exists":
        raise HTTPException(status_code=400, detail="Organization already exists")
    return {"status": "created", "organization": {"organization_name": res["organization_name"], "email": res["email"]}}


@router.get("/org/get")
async def get_org(organization_name: str):
    doc = await get_organization(organization_name)
    if not doc:
        raise HTTPException(status_code=404, detail="Organization not found")
    return doc


@router.put("/org/update")
async def update_org(organization_name: str, new_organization_name: str, admin=Depends(get_current_admin)):
    ok = await update_organization(organization_name, new_organization_name)
    if not ok:
        raise HTTPException(status_code=404, detail="Organization not found or not updated")
    return {"status": "updated"}


@router.delete("/org/delete")
async def delete_org(organization_name: str, admin=Depends(get_current_admin)):
    ok = await delete_organization(organization_name)
    if not ok:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"status": "deleted"}