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
# 定義乖離率的週期、正乖離率臨界值、負乖離率臨界值
BIASPeriod=10
Positive=0.05
Negative=-0.05

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
        # 取得乖離率
        BIAS = KBar1M.GetBIAS(BIASPeriod)
        # 判斷是否有乖離率值
        if len(BIAS) >= BIASPeriod+1:
            BIAS = BIAS[-2]
            print(Time,'Price',Price,'BIAS',BIAS)
            # 超過負乖離率臨界值
            if BIAS <= Negative:
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'價格',Price,'BIAS',BIAS,'多單進場')
                GO.EndSubscribe()
            # 超過正乖離率臨界值
            elif BIAS >= Positive:
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'價格',Price,'BIAS',BIAS,'空單進場')
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
        # 取得乖離率
        BIAS = KBar1M.GetBIAS(BIASPeriod)
        # 判斷是否有乖離率值
        if len(BIAS) >= BIASPeriod+1:
            BIAS = BIAS[-2]
            print(Time,'Price',Price,'BIAS',BIAS)
            # 超過正乖離率臨界值
            if BIAS >= Negative:
                # 多單出場
                if OrderRecord.GetOpenInterest() == 1:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'價格',Price,'BIAS',BIAS,'多單出場')
                    GO.EndSubscribe()
            # 超過負乖離率臨界值
            elif BIAS >= Positive:
                # 空單出場
                if OrderRecord.GetOpenInterest() == -1:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'價格',Price,'BIAS',BIAS,'空單進場')
                    GO.EndSubscribe()

print('全部交易紀錄',OrderRecord.GetTradeRecord())
