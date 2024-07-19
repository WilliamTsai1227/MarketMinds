from model.breaking_info_database import *
from fastapi import FastAPI, APIRouter
from fastapi import *
from fastapi.responses import FileResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from data.fetch_breaking_info import Get_Breaking_info
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
app=FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")

# 創建 FastAPI 應用程式實例
app = FastAPI()
# 設定定時任務
scheduler = BackgroundScheduler()
scheduler.add_job(Get_Breaking_info.scheduled_job, 'cron', hour=8, minute=0)  # 每天早上8點執行
scheduler.start()