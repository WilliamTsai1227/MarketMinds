from fastapi import *
from pydantic import BaseModel,Field
from data.fetch_breaking_info_api import Get_Breaking_info




breaking_info = APIRouter()



# @breaking_info.get("api/breaking_info")

