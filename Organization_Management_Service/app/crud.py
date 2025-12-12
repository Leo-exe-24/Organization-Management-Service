from .db import get_db
from .utils import hash_password, verify_password
from .auth import create_access_token
from bson.objectid import ObjectId

master_db = get_db()

async def organization_exists(org_name: str) -> bool:
    return await master_db.orgs.find_one({"organization_name": org_name}) is not None




async def create_organization(org_name: str, email: str, password: str):
    if await organization_exists(org_name):
        return {"error": "organization_exists"}
    hashed = hash_password(password)
    doc = {
        "organization_name": org_name,
        "email": email,
        "password": hashed,
        "created_at": None,
        "admin": {"email": email}
    }
    res = await master_db.orgs.insert_one(doc)
    doc["_id"] = str(res.inserted_id)
    return doc

async def get_organization(org_name: str):
    doc = await master_db.orgs.find_one({"organization_name": org_name}, {"password": 0})
    if not doc:
        return None
    doc["_id"] = str(doc.get("_id"))
    return doc

async def admin_login(email: str, password: str):
    doc = await master_db.orgs.find_one({"email": email})
    if not doc:
        return None
    hashed = doc.get("password")
    if not verify_password(password, hashed):
        return None
    token = create_access_token({"email": email, "is_admin": True})
    return {"access_token": token}

async def update_organization(org_name: str, new_org_name: str):
    res = await master_db.orgs.update_one({"organization_name": org_name}, {"$set": {"organization_name": new_org_name}})
    return res.modified_count > 0

async def delete_organization(org_name: str):
    res = await master_db.orgs.delete_one({"organization_name": org_name})
    return res.deleted_count > 0