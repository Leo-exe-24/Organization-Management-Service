import motor.motor_asyncio
from .config import MONGO_URI, MONGO_DB


_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
master_db = _client[MONGO_DB]



def get_db():
    return master_db