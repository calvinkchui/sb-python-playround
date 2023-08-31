# 載入相關套件
import sys,haohaninfo,datetime 
from order import Record

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]

# 定義初始倉位
OrderRecord=Record()
# 移動停損點數
StopLoss=0.01

# 訂閱報價
GO = haohaninfo.GOrder.GOQuote()

# 進場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    # 無條件進場多單
    OrderRecord.Order('B',Prod,Time,Price,1)
    # 進場後判斷最高價變數
    AfterOrder=Price
    print(Time,'價格',Price,'無條件進場多單')
    GO.EndSubscribe()

# 出場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    # 判斷移動停損
    if Price > AfterOrder :
        AfterOrder = Price
    elif Price <= AfterOrder * (1-StopLoss):
        # 空單出場
        OrderRecord.Cover('S',Prod,Time,Price,1)
        print(Time,'價格',Price,'進場後最高價',AfterOrder,'移動停損出場')
        GO.EndSubscribe()
        
print('全部交易紀錄',OrderRecord.GetTradeRecord())