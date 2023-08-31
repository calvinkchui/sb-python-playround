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
# 定義MACD週期
FastPeriod=5
SlowPeriod=15
SignalPeriod=5

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
        DIF,MACE,OSC=KBar1M.GetMACD(FastPeriod,SlowPeriod,SignalPeriod)
        # 判斷是否有OSC值
        if len(OSC)>=SlowPeriod+SignalPeriod:
            LastOSC=OSC[-2]
            print(Time,'Price',Price,'LastOSC',LastOSC)
            # OSC偏多
            if LastOSC > 0:
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'OSC',LastOSC,'多單進場')
                GO.EndSubscribe()
            # OSC偏空
            elif LastOSC < 0:
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'OSC',LastOSC,'空單進場')
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
        DIF,MACE,OSC=KBar1M.GetMACD(FastPeriod,SlowPeriod,SignalPeriod)
        # 判斷是否有OSC值
        if len(OSC)>=SlowPeriod+SignalPeriod:
            LastOSC=OSC[-2]
            print(Time,'Price',Price,'LastOSC',LastOSC)
            # 多單出場
            if OrderRecord.GetOpenInterest() == 1:
                # OSC轉空
                if LastOSC < 0:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'OSC',LastOSC,'多單出場')
                    GO.EndSubscribe()       
            # 空單出場
            if OrderRecord.GetOpenInterest() == -1:
                # OSC轉多
                if LastOSC > 0:
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'OSC',LastOSC,'空單出場')
                    GO.EndSubscribe() 
        
print('全部交易紀錄',OrderRecord.GetTradeRecord())
        
