from fastapi import FastAPI, APIRouter
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

#上市個股日收盤價及月平均價

get_stock_price  = APIRouter()
scheduler = BackgroundScheduler()

class Get_Stock_price:
    @staticmethod
    def fetch_data():
        url = "https://openapi.twse.com.tw/v1//exchangeReport/STOCK_DAY_AVG_ALL"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            count = 0
            for item in data:
                stock_code  = item["Code"]
                stock_name = item["Name"]
                closing_price = item["ClosingPrice"]
                monthly_average_price = item["MonthlyAveragePrice"]
                print(f'stock_code:{stock_code},stock_name:{stock_name},closing_price:{closing_price},monthly_average_price:{monthly_average_price}')
                count += 1
            print(count)
            return data
        else:
            print("Failed to fetch data.")
            return False

Get_Stock_price.fetch_data()