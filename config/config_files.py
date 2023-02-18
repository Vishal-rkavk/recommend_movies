import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass

load_dotenv(find_dotenv())
@dataclass(frozen=True)
class APIkeys:
    api_key: str = os.getenv('api_key')
