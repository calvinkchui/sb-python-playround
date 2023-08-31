#載入相關套件及函數
import sys,requests,json

# 取得參數
date=sys.argv[1]

# 外資、自營商、投信彙總表網址
URL='https://www.twse.com.tw/fund/TWT38U?response=json&date='+date
# URL='https://www.twse.com.tw/fund/TWT43U?response=json&date='+date
# URL='https://www.twse.com.tw/fund/TWT44U?response=json&date='+date
 
# 取得網站內容
html= requests.get(URL)

#成功取得網頁
if html.status_code == requests.codes.ok:
    jcontent=json.loads(html.text)
    data=jcontent['data']
    print(data)
else:
    print('爬蟲失敗')





