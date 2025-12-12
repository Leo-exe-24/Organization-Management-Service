from passlib.context import CryptContext
from typing import Optional

_pwd_ctx = CryptContext(schemes=["pbkdf2_sha256", "bcrypt"], deprecated="auto")
MAX_BCRYPT_BYTES = 72

def _to_bytes(s: str) -> bytes:
    return s.encode("utf-8") if isinstance(s, str) else s

def get_active_hash_scheme() -> str:
    try:
        schemes = getattr(_pwd_ctx, "schemes", None)
        if schemes:
            return schemes[0]
    except Exception:
            pass
    return "unknown"

def hash_password(pw: str) -> str:
    if pw is None:
        raise ValueError("password must not be None")
    return _pwd_ctx.hash(pw)




def verify_password(pw: str, hashed: str) -> bool:
    if pw is None or hashed is None:
        return False
    try:
        ok = _pwd_ctx.verify(pw, hashed)
        return ok
    except Exception:
        try:
            from passlib.handlers.bcrypt import bcrypt
            b = _to_bytes(pw)
            if len(b) > MAX_BCRYPT_BYTES:
                truncated = b[:MAX_BCRYPT_BYTES].decode("utf-8", errors="ignore")
                return _pwd_ctx.verify(truncated, hashed)
        except Exception:
            return False
        return False