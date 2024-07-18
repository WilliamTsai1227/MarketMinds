import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
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





# # 發送 GET 請求到目標網頁
# url = 'https://mops.twse.com.tw/mops/web/t05sr01_1'
# response = requests.get(url)

# # 使用 BeautifulSoup 解析網頁內容
# soup = BeautifulSoup(response.content, 'html.parser')

# # 找到 class 为 'hasBorder' 的所有 table 标签
# has_border_tables = soup.find_all('table', class_='hasBorder')

# if has_border_tables:
#     for table in has_border_tables:

#         print(table)
# else:
#     print("未找到 class 为 'hasBorder' 的 table 标签。")

# find_enen_div = soup.findAll('tr', class_='even')

# if find_enen_div:
#     for even in find_enen_div:
#         print(even)


# 设置 ChromeDriver 的路径
driver_path = '/path/to/chromedriver'
service = Service(driver_path)

# 初始化 WebDriver
driver = webdriver.Chrome(service=service)

# 打开目标网页
url = 'https://mops.twse.com.tw/mops/web/t05sr01_1'
driver.get(url)

# 等待页面加载完成
driver.implicitly_wait(10)  # 等待10秒，直到页面加载完成

# 查找 class 为 'even' 的所有 tr 标签
even_rows = driver.find_elements(By.CLASS_NAME, 'even')

if even_rows:
    for row in even_rows:
        # 查找 tr 标签中的 input 按钮
        button = row.find_element(By.XPATH, ".//input[@type='button' and @value='詳細資料']")
        if button:
            # 模拟点击按钮
            button.click()
            
            # 等待新视窗打开
            time.sleep(2)  # 等待2秒，确保新视窗打开
            
            # 切换到新视窗
            driver.switch_to.window(driver.window_handles[-1])
            
            # 抓取新视窗的 HTML 内容
            new_page_html = driver.page_source
            print(new_page_html)
            
            # 可以在这里处理新视窗的数据
            
            # 关闭新视窗
            driver.close()
            
            # 切换回原来的视窗
            driver.switch_to.window(driver.window_handles[0])
else:
    print("未找到 class 为 'even' 的 tr 标签。")

# 关闭浏览器
driver.quit()