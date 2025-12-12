from os import getenv


MONGO_URI = getenv("MONGO_URI", "mongodb://mongo:27017")
MONGO_DB = getenv("MONGO_DB", "org_db")
JWT_SECRET = getenv("JWT_SECRET", "replace-this-secret")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))