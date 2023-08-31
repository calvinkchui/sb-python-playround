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
PowerDiff = int(sys.argv[3])
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
            print(Time,'外盤大於內盤', PowerDiff ,'張觸發多單進場')
            # 多單進場
            OrderRecord.Order('B',Prod,Time,Price,1)
            GO.EndSubscribe()
    elif Price <= DnPrice:
        InDeskAmount += Qty
        if InDeskAmount > OutDeskAmount + PowerDiff:
            print(Time,'內盤大於外盤', PowerDiff ,'張觸發空單進場')
            # 空單進場
            OrderRecord.Order('S',Prod,Time,Price,1)
            GO.EndSubscribe()

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
        if OrderRecord.GetOpenInterest() == -1:
            if InDeskAmount < OutDeskAmount - PowerDiff:
                print(Time,'外盤大於內盤', PowerDiff ,'張觸發空單出場')
                # 空單出場
                OrderRecord.Cover('S',Prod,Time,Price,1)
                GO.EndSubscribe()
    elif Price <= DnPrice:
        InDeskAmount += Qty
        # 多單出場判斷
        if OrderRecord.GetOpenInterest() == -1:
            if OutDeskAmount < InDeskAmount - PowerDiff:
                print(Time,'內盤大於外盤', PowerDiff ,'張觸發空單出場')
                # 多單出場
                OrderRecord.Cover('B',Prod,Time,Price,1)
                GO.EndSubscribe()
        
print('全部交易紀錄',OrderRecord.GetTradeRecord())