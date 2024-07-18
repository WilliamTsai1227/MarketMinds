from fastapi import FastAPI, APIRouter
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
import sys
# 添加當前檔案所在目錄的父目錄到 Python 路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
model_dir = os.path.join(parent_dir, 'model')
# 將 model 資料夾添加到系統路徑
sys.path.append(model_dir)
# 匯入 connection_pool 模組
from connection_pool import connection_pool


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
                # company_name = company['公司名稱']
                # stock_code = company['公司代號']
                # release_date = company['出表日期']
                # event_date = company['事實發生日']
                # title = company['主旨 ']
                # content = company['說明']
                # company_data = {'公司名稱':company_name,'公司代號':type(stock_code),'出表日期':release_date,'事實發生日':event_date,'主旨':title,'說明':content}
                # try:
                #     conn = connection_pool.get_connection()
                #     with conn.cursor() as cursor:
                #         cursor.execute(
                #             """
                #             SELECT id FROM stock_breaking_info WHERE stock_code = %s AND release_date = %s AND event_date = %s AND title = %s
                #             """,
                #             (stock_code,release_date,event_date,title)
                #         )
                #         result = cursor.fetchone() #check if the info already exist
                #         if result == None: 
                #             cursor.execute("INSERT INTO stock_breaking_info (stock_name,stock_code,release_date,event_date,title,content) VALUES (%s,%s,%s,%s,%s,%s)"
                #                             ,(company_name,stock_code,release_date,event_date,title,content))
                #             conn.commit() 
                # except Exception as e:
                #     raise ValueError(f'Wright break_info database error: {e}')
                # finally:
                #     cursor.close()
                #     conn.close()
                return company
        else:
            print("Failed to fetch data.")
            return False
        
Get_Breaking_info.fetch_data()

