import os
import sys
from fastapi import FastAPI, APIRouter
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import yfinance as yf
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from model.connection_pool import connection_pool
from model.stock_price_database import Stock_price_database
import json

#上市個股日收盤價及月平均價

get_stock_price  = APIRouter()
scheduler = BackgroundScheduler()

class Get_Stock_price:
    @staticmethod
    def fetch_data():
        url = "https://openapi.twse.com.tw/v1//exchangeReport/STOCK_DAY_AVG_ALL"
        response = requests.get(url)
        stock_ids = []
        if response.status_code == 200:
            data = response.json()
            for item in data:
                stock_id  = item["Code"]
                stock_name = item["Name"]
                closing_price = item["ClosingPrice"]
                monthly_average_price = item["MonthlyAveragePrice"]
                print(f'stock_code:{stock_id},stock_name:{stock_name},closing_price:{closing_price},monthly_average_price:{monthly_average_price}')
                stock_ids.append(stock_id)
            with open('stock_ids.json', 'w', encoding='utf-8') as f:
                json.dump(stock_ids, f, ensure_ascii=False, indent=4)
            return data
        else:
            print("Failed to fetch data.")
            return False
        
    @staticmethod
    def yahoo_fetch_data(stock_id,stock_name):
        stock_id = '2330'+'.TW'
        # 設定抓取範圍
        end = datetime.today()
        start = end - timedelta(days=360)
        stock_data = yf.download(stock_id, start = start, end = end)
        stock_id = stock_id.split(".")[0]
        Stock_price_database.insert_data(stock_id,stock_name,stock_data)





    @staticmethod
    def save_to_database(id,name,data):
        try:
            conn = connection_pool.get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT DATABASE();")
                record = cursor.fetchone()
                print("Connected to database: ", record)
                create_table_query = """
                CREATE TABLE IF NOT EXISTS stock_prices (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    stock_id VARCHAR(10) NOT NULL,
                    stock_name VARCHAR(20),
                    date DATE NOT NULL,
                    open FLOAT,
                    high FLOAT,
                    low FLOAT,
                    close FLOAT NOT NULL,
                    adj_close FLOAT,
                    volume BIGINT
                )
                """
                cursor.execute(create_table_query)

                # 插入数据
                for index, row in data.iterrows():
                    insert_query = """
                    INSERT INTO stock_prices (stock_id, date, open, high, low, close, adj_close, volume)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_query, (
                        id, index.date(), row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']
                    ))
                conn.commit()
                print("Data inserted successfully")
        except Exception as e:
            print("Error while connecting to MySQL", e)
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection is closed")

# # 获取股票数据
# stock_data = Get_Stock_price.yahoo_fetch_data()

# # 将股票数据存入数据库
# Get_Stock_price.save_to_database(stock_data)
Get_Stock_price.fetch_data()
