from fastapi import FastAPI, APIRouter
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from model.connection_pool import connection_pool
from model.breaking_info_database import Breaking_info_database


get_breaking_info  = APIRouter()
scheduler = BackgroundScheduler()

class Get_Breaking_info:
    @staticmethod
    def fetch_data():
        url = "https://openapi.twse.com.tw/v1/opendata/t187ap04_L"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for company in data:
                try:
                    Breaking_info_database.insert_data(company)
                except Exception as e:
                    raise ValueError(f'Write break_info database error: {e}')
        else:
            print("Failed to fetch data.")
            return False
        
    # 定義定時任務
    @staticmethod
    def scheduled_job():
        print("Fetching data at", datetime.now())
        Get_Breaking_info.fetch_data()
Get_Breaking_info.fetch_data()