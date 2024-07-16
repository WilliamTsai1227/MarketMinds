from fastapi import *
from pydantic import BaseModel,Field
from data.get_breaking_company_info import Get_Breaking_info




breaking_info = APIRouter()



# @breaking_info.get("api/breaking_info")

