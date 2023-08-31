#載入相關套件及函數
import sys,requests
from bs4 import BeautifulSoup

# 網址
URL='https://www.taifex.com.tw/cht/9/futuresQADetail'

# 取得網站內容
html= requests.get(URL)

#成功取得網頁
if html.status_code == requests.codes.ok:
    # 透過 BeautifulSoup 解析該網站
    soup=BeautifulSoup(html.text,'html.parser')
    # 取得表格內資訊
    rs_list=[]
    for tr in soup.find_all('tr',bgcolor='#FFFFFF'):
        # 移除特殊符號
        tr_content = [ i.text.strip() for i in tr.find_all('td') ]
        # 取出前後兩個部分
        first_stock=tr_content[:4]
        second_stock=tr_content[4:8]
        # 新增至統一的List中
        rs_list.append(first_stock)
        rs_list.append(second_stock)
    # 依照排名排序
    sorted(rs_list,key=lambda x: int(x[0])  , reverse=False)
    print(rs_list)
else:
    print('爬蟲失敗')





