# 載入相關套件
import sys,haohaninfo,datetime,numpy
from order import Record
from indicator import KBar

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]
# 定義初始倉位
OrderRecord=Record()
# 定義K棒物件
Today=datetime.datetime.now().strftime('%Y%m%d')
KBar1M=KBar(Today,1)
# 定義RSI週期
Period=10
# 移動停損點數
StopLoss=0.02

# 訂閱報價
GO = haohaninfo.GOrder.GOQuote()
# 進場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    Qty=float(row[3])
    ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
    # 每分鐘判斷一次
    if ChangeKFlag==1:
        # 取得RSI
        RSI=KBar1M.GetRSI(Period)
        # 判斷是否有RSI值
        if len(RSI) >= Period+1:
            LastRSI=RSI[-2]
            print(Time,'Price',Price,'LastRSI',LastRSI)
            # RSI小於20
            if LastRSI < 20:
                OrderPrice=Price
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'多單進場',Prod,Time,Price)
                GO.EndSubscribe()
            # RSI大於80
            elif LastRSI > 80:
                OrderPrice=Price
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'空單進場',Prod,Time,Price)
                GO.EndSubscribe()
        
# 多單出場判斷
if OrderRecord.GetOpenInterest() == 1:
    # 移動停損基準
    StopLossPoint=OrderPrice
    # 出場判斷
    for row in GO.Subscribe( Broker, 'match', Prod ):    
        # 取得時間、價格欄位
        Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        Price=float(row[2])
        Qty=float(row[3])
        ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
        # 每分鐘判斷一次
        if ChangeKFlag==1:
            # 更新當前的移動停損基準
            StopLossPoint=max(StopLossPoint,Price)
            # 取得RSI
            RSI=KBar1M.GetRSI(Period)
            # 判斷是否有RSI值
            if len(RSI) >= Period+1:
                LastRSI=RSI[-2]
                print(Time,'Price',Price,'LastRSI',LastRSI)
                # RSI回歸70
                if LastRSI > 70:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'RSI回檔',Prod,Time,Price)
                    GO.EndSubscribe()
                # 移動停損判斷
                elif Price <= StopLossPoint*(1-StopLoss):
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'移動停損',Prod,Time,Price)
                    GO.EndSubscribe()        
# 空單出場判斷
if OrderRecord.GetOpenInterest() == -1: 
    # 移動停損基準
    StopLossPoint=OrderPrice
    # 出場判斷
    for row in GO.Subscribe( Broker, 'match', Prod ):    
        # 取得時間、價格欄位
        Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
        Price=float(row[2])
        Qty=float(row[3])
        ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
        # 每分鐘判斷一次
        if ChangeKFlag==1:
            # 更新當前的移動停損基準
            StopLossPoint=min(StopLossPoint,Price)
            # 取得RSI
            RSI=KBar1M.GetRSI(Period)
            # 判斷是否有RSI值
            if len(RSI) >= Period+1:
                LastRSI=RSI[-2]
                print(Time,'Price',Price,'LastRSI',LastRSI)
                # RSI回歸30
                if LastRSI < 30:
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'RSI回檔',Prod,Time,Price)
                    GO.EndSubscribe()
                # 移動停損判斷
                elif Price >= StopLossPoint*(1+StopLoss):
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'移動停損',Prod,Time,Price)
                    GO.EndSubscribe()    
    
print('全部交易紀錄',OrderRecord.GetTradeRecord())