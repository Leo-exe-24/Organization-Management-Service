#!/usr/bin/env python3

import requests
import json
import sys
import time
from datetime import datetime, timezone

BASE = "http://127.0.0.1:8000"
HEADERS_JSON = {"Content-Type": "application/json"}


def pp(title, data):
    print("\n" + "="*8 + f" {title} " + "="*8)
    try:
        print(json.dumps(data, indent=2))
    except Exception:
        print(data)


def fail(msg):
    print("\n❌", msg)
    sys.exit(1)


def try_request(method, url, **kwargs):
    try:
        r = requests.request(method, url, timeout=30, **kwargs)
        try:
            body = r.json()
        except Exception:
            body = r.text
        return r.status_code, body
    except Exception as e:
        fail(f"Request to {url} failed: {e}")


def unique_org_name(prefix="testorg"):
    now = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return f"{prefix}_{now}"


def main():
    print("Integration test starting. BASE =", BASE)

    org_name = unique_org_name()
    email = f"admin+{org_name}@example.com"
    password = "Pass123!"

    # 1) Create organization
    payload_create = {
        "organization_name": org_name,
        "email": email,
        "password": password
    }
    status, body = try_request("POST", f"{BASE}/org/create", json=payload_create, headers=HEADERS_JSON)
    pp("Create Organization response", {"status": status, "body": body})
    if status not in (200, 201):
        fail(f"Create organization failed (status {status}).")

    # 2) Get organization
    status, body = try_request("GET", f"{BASE}/org/get", params={"organization_name": org_name})
    pp("Get Organization response", {"status": status, "body": body})
    if status != 200:
        fail("Get organization failed after create.")

    # 3) Admin login
    payload_login = {"email": email, "password": password}
    status, body = try_request("POST", f"{BASE}/admin/login", json=payload_login, headers=HEADERS_JSON)
    pp("Admin Login response", {"status": status, "body": body})
    if status != 200:
        fail("Admin login failed.")

    token = None
    if isinstance(body, dict):
        token = body.get("access_token") or body.get("token")
    if not token:
        fail("Login did not return access_token.")

    auth_header = {"Authorization": f"Bearer {token}"}

    # 4) Update organization (rename)
    new_org_name = org_name + "_renamed"
    status, body = try_request("PUT",
                              f"{BASE}/org/update",
                              params={"organization_name": org_name, "new_organization_name": new_org_name},
                              headers=auth_header)
    pp("Update (rename) Organization response", {"status": status, "body": body})
    if status not in (200, 201):
        fail("Rename failed.")

    time.sleep(1)

    # 5) Verify organization info with new name
    status, body = try_request("GET", f"{BASE}/org/get", params={"organization_name": new_org_name})
    pp("Get Organization (after rename) response", {"status": status, "body": body})
    if status != 200:
        fail("Renamed organization not found.")

    # 6) Delete organization (using admin token)
    status, body = try_request("DELETE",
                              f"{BASE}/org/delete",
                              params={"organization_name": new_org_name},
                              headers=auth_header)
    pp("Delete Organization response", {"status": status, "body": body})
    if status not in (200, 204):
        fail("Delete failed.")

    # 7) Verify deletion (should not be 200)
    status, body = try_request("GET", f"{BASE}/org/get", params={"organization_name": new_org_name})
    pp("Get Organization (after delete) response", {"status": status, "body": body})
    if status == 200:
        fail("Organization still exists after delete.")
    else:
        print("\n✅ Integration flow passed.")

if __name__ == "__main__":
    main()