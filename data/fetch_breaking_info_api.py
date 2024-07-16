from fastapi import FastAPI, APIRouter
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


get_breaking_info  = APIRouter()
scheduler = BackgroundScheduler()

class Get_Breaking_info:
    @staticmethod
    def fetch_data():
        url = "https://openapi.twse.com.tw/v1/opendata/t187ap04_L"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to fetch data.")
            return False
