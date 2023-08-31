# 載入相關套件
import haohaninfo,indicator,datetime,time,sys
from screen import GetNumberStockDaily

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]
# 取得前一日收盤價資訊
LastDayInfo=GetNumberStockDaily(1,Prod)[-1]
LastClose=LastDayInfo[4]
# 跳空區間
UpGap=1.01
DnGap=0.99
# 停損停利區間
TakeProfit=0.09
StopLoss=0.03
# 定義要進出場的時間(9:01以前進場 13:20出場)
InTime=datetime.datetime.now().replace( hour=9 , minute=1 , second=00 , microsecond=00 )
OutTime=datetime.datetime.now().replace( hour=13 , minute=20 , second=00 , microsecond=00 )

# 定義初始倉位
OrderRecord=Record()

# 進場判斷邏輯
GO = haohaninfo.GOrder.GOQuote()
# 訂閱報價
for row in GO.Subscribe(Broker, 'match', Prod):
    # 定義時間
    Time = datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    # 定義成交價
    Price=float(row[2])
    # 判斷時間是否小於進場時間
    if Time < InTime:
        # 判斷價格跳空(需要在開盤前就預先等待報價判斷開盤跳空判斷)
        if Price > LastClose * UpGap:
            # 進場多單
            OrderPrice=Price
            OrderRecord.Order('B',Prod,Time,Price,1)
            print(Time,'向上跳空進場買',Prod,Time,Price)
        elif Price < LastClose * DnGap:
            # 進場空單
            OrderPrice=Price
            OrderRecord.Order('S',Prod,Time,Price,1)
            print(Time,'向下跳空進場賣',Prod,Time,Price)
    # 判斷完成以後跳出迴圈
    GO.EndSubscribe()

# 空手則停止策略
if OrderRecord.GetOpenInterest() == 0:
    print('當日無進場交易')
# 多單出場邏輯
if OrderRecord.GetOpenInterest() == 1:
    # 訂閱報價物件
    GO = haohaninfo.GOrder.GOQuote()
    # 訂閱報價
    for row in GO.Subscribe(Broker, 'match', Prod):
        # 定義時間
        Time = datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        # 定義成交價
        Price=float(row[2])
        # 判斷停利
        if Price > OrderPrice * (1+TakeProfit):
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'停利',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 判斷停損
        elif Price < OrderPrice * (1-StopLoss):
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'停損',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 判斷到期出場
        elif Time > OutTime:
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'到期',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
# 空單出場邏輯
if OrderRecord.GetOpenInterest() == -1:
    # 訂閱報價物件
    GO = haohaninfo.GOrder.GOQuote()
    # 訂閱報價
    for row in GO.Subscribe(Broker, 'match', Prod):
        # 定義時間
        Time = datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        # 定義成交價
        Price=float(row[2])
        # 判斷停利
        if Price < OrderPrice * (1-TakeProfit):
            # 多單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'停利',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 判斷停損
        elif Price > OrderPrice * (1+StopLoss):
            # 多單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'停損',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 判斷到期出場
        elif Time > OutTime:
            # 多單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'到期',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()

print('全部交易紀錄',OrderRecord.GetTradeRecord())