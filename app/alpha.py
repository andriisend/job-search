import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")
user_agent = os.getenv("user_agent")
