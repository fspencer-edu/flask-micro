import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REDIS_HOST = os.environ["REDIS_HOST"]
    REDIS_PORT = int(os.environ["REDIS_PORT"])