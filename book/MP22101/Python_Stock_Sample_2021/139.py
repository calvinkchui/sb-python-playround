# 載入相關套件
import haohaninfo,indicator,datetime,time,sys
from order import Record

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]
# 定義內外盤總量、差距
OutDeskAmount=0
InDeskAmount=0
PowerDiff = 2000
# 停利區間
TakeProfit=0.09
# 定義要進出場的時間(13:20出場)
OutTime=datetime.datetime.now().replace( hour=13 , minute=20 , second=00 , microsecond=00 )

# 定義初始倉位
OrderRecord=Record()
    
# 訂閱報價
GO = haohaninfo.GOrder.GOQuote()
# 進場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    # 定義成交價、成交量、買價、賣價
    Price=float(row[2])
    Qty=int(row[3])
    DnPrice=float(row[5])
    UpPrice=float(row[6])
    # 內外盤判斷
    if Price >= UpPrice:
        OutDeskAmount += Qty
        if OutDeskAmount > InDeskAmount + PowerDiff:
            # 多單進場
            OrderPrice=Price
            OrderRecord.Order('B',Prod,Time,Price,1)
            print(Time,'外盤大於內盤', PowerDiff ,'張觸發多單進場',Prod,Time,Price)
            GO.EndSubscribe()
    elif Price <= DnPrice:
        InDeskAmount += Qty
        if InDeskAmount > OutDeskAmount + PowerDiff:
            # 空單進場
            OrderPrice=Price
            OrderRecord.Order('S',Prod,Time,Price,1)
            print(Time,'內盤大於外盤', PowerDiff ,'張觸發空單進場',Prod,Time,Price)
            GO.EndSubscribe()

# 多單出場邏輯
if OrderRecord.GetOpenInterest() == 1:
    # 出場判斷
    for row in GO.Subscribe( Broker, 'match', Prod ):    
        # 取得時間
        Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        # 定義成交價、成交量、買價、賣價
        Price=float(row[2])
        Qty=int(row[3])
        DnPrice=float(row[5])
        UpPrice=float(row[6])
        # 內外盤判斷
        if Price >= UpPrice:
            OutDeskAmount += Qty
        elif Price <= DnPrice:
            InDeskAmount += Qty
            # 多單出場判斷
            if OutDeskAmount < InDeskAmount:
                print(Time,'內外盤反轉出場',Prod,Time,Price)
                # 多單出場
                OrderRecord.Cover('S',Prod,Time,Price,1)
                GO.EndSubscribe()
        # 停利判斷
        if Price > OrderPrice * (1+TakeProfit):
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'停利',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 到期出場判斷
        elif Time > OutTime:
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'到期',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
# 空單出場邏輯
if OrderRecord.GetOpenInterest() == -1:
    # 出場判斷
    for row in GO.Subscribe( Broker, 'match', Prod ):    
        # 取得時間
        Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        # 定義成交價、成交量、買價、賣價
        Price=float(row[2])
        Qty=int(row[3])
        DnPrice=float(row[5])
        UpPrice=float(row[6])
        # 內外盤判斷
        if Price >= UpPrice:
            OutDeskAmount += Qty
            # 空單出場判斷
            if OutDeskAmount < InDeskAmount:
                print(Time,'內外盤反轉出場',Prod,Time,Price)
                # 多單出場
                OrderRecord.Cover('B',Prod,Time,Price,1)
                GO.EndSubscribe()
        elif Price <= DnPrice:
            InDeskAmount += Qty
        # 停利判斷
        if Price < OrderPrice * (1-TakeProfit):
            # 多單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'停利',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
        # 到期出場判斷
        elif Time > OutTime:
            # 多單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'到期',Prod,Time,Price)
            # 判斷完成以後跳出迴圈
            GO.EndSubscribe()
            
print('全部交易紀錄',OrderRecord.GetTradeRecord())