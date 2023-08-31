#載入相關套件及函數
import sys,requests
from bs4 import BeautifulSoup

# 單日買超排行
URL='https://tw.stock.yahoo.com/d/i/sebuy_tse.html'
# 上週買超排行
# URL='https://tw.stock.yahoo.com/d/i/sebuy_tse_w.html'
# 單日賣超排行
# URL='https://tw.stock.yahoo.com/d/i/sesell_tse.html'
# 上週賣超排行
# URL='https://tw.stock.yahoo.com/d/i/sesell_tse_w.html'


# 取得網站內容
html= requests.get(URL)

#成功取得網頁
if html.status_code == requests.codes.ok:
    # 透過 BeautifulSoup 解析該網站
    soup=BeautifulSoup(html.text,'html.parser')
    # 取得表格內資訊
    for tr in soup.find_all('tr',bgcolor='#FFFFFF'):
        tr_content = [ i.text for i in tr.find_all('td') ]
        print(tr_content)
else:
    print('爬蟲失敗')





