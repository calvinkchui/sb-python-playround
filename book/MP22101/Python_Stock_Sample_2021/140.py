# 載入相關套件
import sys,haohaninfo,datetime,numpy
from order import Record
from indicator import KBar

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]
# 定義K棒物件
Today=datetime.datetime.now().strftime('%Y%m%d')
KBar1M=KBar(Today,1)
# 定義MA週期
FastPeriod=12
SlowPeriod=16
# 定義KD週期
RSVPeriod=5
KPeriod=3
DPeriod=3
# 移動停損點數
StopLoss=0.02

# 定義初始倉位
OrderRecord=Record()

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
        FastMA=KBar1M.GetWMA(FastPeriod)
        SlowMA=KBar1M.GetWMA(SlowPeriod)
        K,D=KBar1M.GetKD(RSVPeriod,KPeriod,DPeriod)
        # 判斷是否有MA、KD值
        if len(SlowMA)>=SlowPeriod+1 and len(K) >= RSVPeriod+KPeriod+1:
            LastFastMA=FastMA[-2]
            LastSlowMA=SlowMA[-2]
            LastK=K[-2]
            LastD=D[-2]
            print(Time,'LastFastMA',LastFastMA,'LastSlowMA',LastSlowMA,'LastK',LastK,'LastD',LastD)
            # MA快線大於慢線 並且 K > D
            if LastFastMA > LastSlowMA and LastK > LastD :
                OrderPrice=Price
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'多單進場',Prod,Time,Price)
                GO.EndSubscribe()
            # MA快線低於慢線 並且 K < D
            elif LastFastMA < LastSlowMA and LastK < LastD :
                OrderPrice=Price
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'空單進場',Prod,Time,Price)
                GO.EndSubscribe()

# 多單出場邏輯
if OrderRecord.GetOpenInterest() == 1:
    # 移動停損基準
    StopLossPoint=OrderPrice
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
            FastMA=KBar1M.GetWMA(FastPeriod)
            SlowMA=KBar1M.GetWMA(SlowPeriod)
            K,D=KBar1M.GetKD(RSVPeriod,KPeriod,DPeriod)
            print(Time,'LastFastMA',LastFastMA,'LastSlowMA',LastSlowMA,'LastK',LastK,'LastD',LastD)
            # 判斷是否有MA、KD值
            if len(SlowMA)>=SlowPeriod+1:
                LastFastMA=FastMA[-2]
                LastSlowMA=SlowMA[-2]
                LastK=K[-2]
                LastD=D[-2]
                print(Time,'LastFastMA',LastFastMA,'LastSlowMA',LastSlowMA,'LastK',LastK,'LastD',LastD)
                # MA快線低於慢線 並且 K < D
                if LastFastMA < LastSlowMA and LastK < LastD :
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'指標反轉',Prod,Time,Price)
                    GO.EndSubscribe()
                # 移動停損判斷
                elif Price <= StopLossPoint*(1-StopLoss):
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'移動停損',Prod,Time,Price)
                    GO.EndSubscribe()
# 空單出場邏輯
if OrderRecord.GetOpenInterest() == -1:
    # 移動停損基準
    StopLossPoint=OrderPrice
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
            FastMA=KBar1M.GetWMA(FastPeriod)
            SlowMA=KBar1M.GetWMA(SlowPeriod)
            K,D=KBar1M.GetKD(RSVPeriod,KPeriod,DPeriod)
            print(Time,'LastFastMA',LastFastMA,'LastSlowMA',LastSlowMA,'LastK',LastK,'LastD',LastD)
            # 判斷是否有MA、KD值
            if len(SlowMA)>=SlowPeriod+1:
                LastFastMA=FastMA[-2]
                LastSlowMA=SlowMA[-2]
                LastK=K[-2]
                LastD=D[-2]
                print(Time,'LastFastMA',LastFastMA,'LastSlowMA',LastSlowMA,'LastK',LastK,'LastD',LastD)
                # MA快線高於慢線 並且 K > D
                if LastFastMA > LastSlowMA and LastK > LastD :
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'指標反轉',Prod,Time,Price)
                    GO.EndSubscribe()
                # 移動停損判斷
                elif Price >= StopLossPoint*(1+StopLoss):
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'移動停損',Prod,Time,Price)
                    GO.EndSubscribe()
                    
print('全部交易紀錄',OrderRecord.GetTradeRecord())
        
