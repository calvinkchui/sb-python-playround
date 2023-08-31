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
# 定義威廉指標的週期、超買區、超賣區
WILLRPeriod=7
OverBuy = -20
OverSell = -80

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
        # 取得威廉指標
        WILLR=KBar1M.GetWILLR(WILLRPeriod)
        # 判斷是否有威廉指標值
        if len(WILLR) >= WILLRPeriod+1:
            ThisWILLR=WILLR[-2]
            LastWILLR=WILLR[-3]
            print(Time,'Price',Price,'ThisWILLR',ThisWILLR)
            # 進入超賣區 並且回檔
            if ThisWILLR > OverSell and LastWILLR <= OverSell:
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'價格',Price,'ThisWILLR',ThisWILLR,'多單進場')
                GO.EndSubscribe()
            # 進入超買區 並且回檔
            elif ThisWILLR < OverBuy and LastWILLR >= OverBuy:
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'價格',Price,'ThisWILLR',ThisWILLR,'空單進場')
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
        # 取得威廉指標
        WILLR=KBar1M.GetWILLR(WILLRPeriod)
        # 判斷是否有威廉指標值
        if len(WILLR) >= WILLRPeriod+1:
            ThisWILLR=WILLR[-2]
            LastWILLR=WILLR[-3]
            print(Time,'Price',Price,'ThisWILLR',ThisWILLR)
            # 多單出場
            if OrderRecord.GetOpenInterest() == 1:
                # 進入超買區 並且回檔
                if ThisWILLR < OverBuy and LastWILLR >= OverBuy:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'價格',Price,'ThisWILLR',ThisWILLR,'多單出場')
                    GO.EndSubscribe()
            # 空單出場
            if OrderRecord.GetOpenInterest() == -1:
                # 進入超賣區 並且回檔
                if ThisWILLR > OverSell and LastWILLR <= OverSell:
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'價格',Price,'ThisWILLR',ThisWILLR,'空單出場')
                    GO.EndSubscribe()
    
print('全部交易紀錄',OrderRecord.GetTradeRecord())