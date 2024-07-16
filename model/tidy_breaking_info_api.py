import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from data.fetch_breaking_info_api import Get_Breaking_info

data = Get_Breaking_info.fetch_data()


# 直接使用 data 作為列表
for company in data:
    release_date = company['出表日期']
    incident_date = company['事實發生日']
    company_name = company['公司名稱']
    stock_code = company['公司代號']
    title = company['主旨 ']
    content = company['說明']
    print(f'公司名稱：{company_name}，股票代碼：{stock_code}，出表日期：{release_date}，事實發生日：{incident_date}，主旨：{title}，內容：{content}')



# # 解析 JSON 資料
# parsed_data = json.loads(data)
