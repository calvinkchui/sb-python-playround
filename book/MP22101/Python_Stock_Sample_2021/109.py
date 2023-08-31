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
# 定義KD週期
RSVPeriod=9
KPeriod=3
DPeriod=3

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
        # 取得KD
        K,D=KBar1M.GetKD(RSVPeriod,KPeriod,DPeriod)
        # 判斷是否有KD值
        if len(K) >= RSVPeriod+KPeriod+1:
            LastK=K[-2]
            LastD=D[-2]
            print(Time,'Price',Price,'LastK',LastK,'LastD',LastD)
            # K值大於D值
            if LastK > LastD:
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'價格',Price,'K',LastK,'D',LastD,'多單進場')
                GO.EndSubscribe()
            # K值小於D值
            elif LastK < LastD:
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'價格',Price,'K',LastK,'D',LastD,'多單進場')
                GO.EndSubscribe()
        
# 出場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    Qty=float(row[3])
    ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
    # 每分鐘判斷一次
    if ChangeKFlag==1:
        # 取得KD
        K,D=KBar1M.GetKD(RSVPeriod,KPeriod,DPeriod)
        # 判斷是否有KD值
        if len(K) >= RSVPeriod+KPeriod+1:
            LastK=K[-2]
            LastD=D[-2]
            print(Time,'Price',Price,'LastK',LastK,'LastD',LastD)
            # 多單出場
            if OrderRecord.GetOpenInterest() == 1:
                # K值小於D值
                if LastK < LastD:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'價格',Price,'K',LastK,'D',LastD,'多單出場')
                    GO.EndSubscribe()
            # 空單出場
            if OrderRecord.GetOpenInterest() == -1:
                # K值大於D值
                if LastK > LastD:
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'價格',Price,'K',LastK,'D',LastD,'空單出場')
                    GO.EndSubscribe()
    
print('全部交易紀錄',OrderRecord.GetTradeRecord())