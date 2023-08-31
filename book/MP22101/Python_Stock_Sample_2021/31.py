import sys,requests,json

# 取得參數
date=sys.argv[1]
stock_symbol=sys.argv[2]

# 取得網站內容
html= requests.get('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+stock_symbol)

#成功取得網頁
if html.status_code == requests.codes.ok:
    jcontent=json.loads(html.text)
    data=jcontent['data']
    print(data)
else:
    print('爬蟲失敗')





