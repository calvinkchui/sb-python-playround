# 載入相關套件
import sys
import haohaninfo,indicator,datetime,time,sys
from screen import GetTAStockDaily
from talib.abstract import SMA

# 選擇報價平台
Broker = sys.argv[1]
# 取得股票代碼
Prod = sys.argv[2]
# 取得要計算MA的時間週期
Number = int(sys.argv[3])

# 取得N日的股票日資料
TAKBar=GetTAStockDaily(Number,Prod)

# 計算移動平均線
SMA=SMA(TAKBar, timeperiod=Number)[-1]

# 訂閱報價物件
GO = haohaninfo.GOrder.GOQuote()
# 訂閱報價
for row in GO.Subscribe(Broker, 'match', Prod):
    # 定義時間
    Time = datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    # 定義成交價
    Price=float(row[2])
    # 判斷價格與日移動平均的關係
    if Price > SMA:
        print(Time,'價格',Price,'大於',Number,'日MA',SMA)
    elif Price < SMA:
        print(Time,'價格',Price,'小於',Number,'日MA',SMA)
    # 判斷完成以後跳出迴圈
    GO.EndSubscribe()