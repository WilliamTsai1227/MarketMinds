import requests
from bs4 import BeautifulSoup
# url = 'https://mops.twse.com.tw/server-java/AjaxCheck'
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Accept': 'text/html;charset=Big5',  # 根据需要设置接受的内容类型
#     # 其他可能需要的请求头
# }
# data = {
#     'param1': 'value1',
#     'param2': 'value2'
# }

# response = requests.post(url, headers=headers, data=data)

# if response.status_code == 200:
#     print('Request successful')
#     print('Response content:', response.text)  # 输出响应内容
# else:
#     print('Request failed with status code:', response.status_code)
#     print('Response content:', response.text)  # 输出错误时的响应内容


# headers = {
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Host': 'mops.twse.com.tw',
#     'Origin': 'https://mops.twse.com.tw',
#     'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"macOS"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
# }

# cookies = {
#     'jcsession': 'jHttpSession@7c0d670c',
#     '_ga': 'GA1.1.875455021.1721144037',
#     '_ga_LTMT28749H': 'GS1.1.1721144037.1.1.1721144062.0.0.0'
# }

# data = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# response = requests.post('https://mops.twse.com.tw/mops/web/t05st02', headers=headers, cookies=cookies, data=data)
# print(response.text)





# 發送 GET 請求到目標網頁
url = 'https://mops.twse.com.tw/mops/web/t05st02'
response = requests.get(url)

# 使用 BeautifulSoup 解析網頁內容
soup = BeautifulSoup(response.content, 'html.parser')

# 找到 id 為 'PageBody' 的 div 標籤
page_body_div = soup.find('div', id='PageBody')

if page_body_div:
    # 打印 div 內容
    print(page_body_div.text.strip())
else:
    print("未找到 id 為 'PageBody' 的 div 標籤。")
