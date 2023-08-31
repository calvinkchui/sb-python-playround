#載入相關套件及函數
import sys,requests
from bs4 import BeautifulSoup

# 取得參數
t=sys.argv[1]
e=sys.argv[2]
n=sys.argv[3]

# 網址
URL='https://tw.stock.yahoo.com/d/i/rank.php?t='+t+'&e='+e+'&n='+n

# 取得網站內容
html= requests.get(URL)

#成功取得網頁
if html.status_code == requests.codes.ok:
    # 透過 BeautifulSoup 解析該網站
    soup=BeautifulSoup(html.text,'html.parser')
    # 取得表格內資訊
    for tr in soup.find_all('tr',bgcolor='#ffffff'):
        tr_content = [ i.text for i in tr.find_all('td') ]
        print(tr_content)
else:
    print('爬蟲失敗')





