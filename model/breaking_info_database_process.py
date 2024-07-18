import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from data.fetch_breaking_info import Get_Breaking_info
from model.connection_pool import connection_pool
data = Get_Breaking_info.fetch_data()


class Breaking_info_database:
    @staticmethod
    def insert_data(company):
        try:
            company_name = company['公司名稱']
            stock_code = company['公司代號']
            release_date = company['出表日期']
            event_date = company['事實發生日']
            title = company['主旨 ']
            content = company['說明']
            conn = connection_pool.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id FROM stock_breaking_info WHERE stock_code = %s AND release_date = %s AND event_date = %s AND title = %s
                    """,
                    (stock_code,release_date,event_date,title)
                )
                result = cursor.fetchone() #check if the info already exist
                if result == None: 
                    cursor.execute("INSERT INTO stock_breaking_info (stock_name,stock_code,release_date,event_date,title,content) VALUES (%s,%s,%s,%s,%s,%s)"
                                    ,(company_name,stock_code,release_date,event_date,title,content))
                    conn.commit() 
        except Exception as e:
            raise ValueError(f'Wright break_info database error: {e}')
        finally:
            cursor.close()
            conn.close()