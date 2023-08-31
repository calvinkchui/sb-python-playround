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
# 定義MA週期
FastPeriod=9
SlowPeriod=16
# MA穿越次數
CrossFlag=0
# 預設趨勢
Trend=1

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
        # 判斷是否有MA值
        if len(SlowMA)>=SlowPeriod+2:
            Last1FastMA,Last2FastMA=FastMA[-2],FastMA[-3]
            Last1SlowMA,Last2SlowMA=SlowMA[-2],SlowMA[-3]    
            print(Time,'Price',Price,'LastFastMA',Last1FastMA,'LastSlowMA',Last1SlowMA)
            # 趨勢為多方
            if Trend==1: 
                # 快線穿越慢線
                if Last1FastMA > Last1SlowMA and Last2FastMA < Last2SlowMA :
                    CrossFlag+=1
                    # 穿越第二次
                    if CrossFlag == 2:
                        OrderRecord.Order('B',Prod,Time,Price,1)
                        print(Time,'快線',Last1FastMA,'慢線',Last1SlowMA,'多單進場')
                        GO.EndSubscribe()
            # 趨勢為空方
            if Trend==-1:     
                # 快線穿越慢線
                if Last1FastMA < Last1SlowMA and Last2FastMA > Last2SlowMA :
                    CrossFlag+=1
                    # 穿越第二次
                    if CrossFlag == 2:
                        OrderRecord.Order('S',Prod,Time,Price,1)
                        print(Time,'快線',Last1FastMA,'慢線',Last1SlowMA,'空單進場')
                        GO.EndSubscribe()

# 定義要進出場的時間(11:30出場)
OutTime=datetime.datetime.now().replace( hour=11 , minute=30 , second=00 , microsecond=00 )        

# 出場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    # 到出場時間後出場
    if Time >= OutTime:
        if OrderRecord.GetOpenInterest() == 1:
            # 多單出場
            OrderRecord.Cover('S',Prod,Time,Price,1)
            print(Time,'時間到出場')
            GO.EndSubscribe()       
        if OrderRecord.GetOpenInterest() == -1:
            # 空單出場
            OrderRecord.Cover('B',Prod,Time,Price,1)
            print(Time,'時間到出場')
            GO.EndSubscribe()      
        
print('全部交易紀錄',OrderRecord.GetTradeRecord())