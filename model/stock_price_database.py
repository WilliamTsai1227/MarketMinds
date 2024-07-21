from model.connection_pool import connection_pool

class Stock_price_database:
    @staticmethod
    def insert_data(id,name,data):
        try:
            company_name = company['公司名稱']
            stock_id = company['公司代號']
            release_date = company['出表日期']
            speech_date = company['發言日期']
            speech_time = company['發言時間']
            event_date = company['事實發生日']
            title = company['主旨 '].replace('\r\n', ' ').replace('\n', ' ')
            content = company['說明'].replace('\r\n', ' ').replace('\n', ' ')
            conn = connection_pool.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT id FROM stock_breaking_info WHERE stock_id = %s AND release_date = %s AND speech_date = %s AND speech_time = %s AND title = %s
                    """,
                    (stock_id,release_date,speech_date,speech_time,title)
                )
                result = cursor.fetchone() #check if the info already exist
                if result == None: 
                    cursor.execute("INSERT INTO stock_breaking_info (stock_name,stock_id,release_date,event_date,speech_date,speech_time,title,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                                    ,(company_name,stock_id,release_date,event_date,speech_date,speech_time,title,content))
                    conn.commit() 
        except Exception as e:
            raise ValueError(f'Write break_info database error: {e}')
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()