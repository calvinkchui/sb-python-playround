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
# 定義布林通道週期
Period=10

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
        # 取得布林通道上下界
        Upper,Middle,Lower=KBar1M.GetBBands(Period)
        # 判斷是否有布林通道值
        if len(Upper) >= Period+1:
            LastUpper=Upper[-2]
            LastLower=Lower[-2]
            print(Time,'Price',Price,'LastUpper',LastUpper,'LastLower',LastLower)
            # 價格觸及下界
            if Price <= LastLower:
                OrderRecord.Order('B',Prod,Time,Price,1)
                print(Time,'價格',Price,'布林通道下界',LastLower,'多單進場')
                GO.EndSubscribe()
            # 價格觸及上界
            elif Price >= LastUpper:
                OrderRecord.Order('S',Prod,Time,Price,1)
                print(Time,'價格',Price,'布林通道上界',LastUpper,'空單進場')
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
        # 取得布林通道上下界
        Upper,Middle,Lower=KBar1M.GetBBands(Period)
        # 判斷是否有布林通道值
        if len(Upper) >= Period+1:
            LastUpper=Upper[-2]
            LastLower=Lower[-2]
            print(Time,'Price',Price,'LastUpper',LastUpper,'LastLower',LastLower)
            # 多單出場
            if OrderRecord.GetOpenInterest() == 1:
                # 價格反彈至上界
                if Price >= LastUpper:
                    OrderRecord.Cover('S',Prod,Time,Price,1)
                    print(Time,'價格',Price,'布林通道上界',LastUpper,'多單出場')
                    GO.EndSubscribe()
            # 空單出場
            if OrderRecord.GetOpenInterest() == -1:
                # 價格反彈至下界
                if Price <= LastLower:
                    OrderRecord.Cover('B',Prod,Time,Price,1)
                    print(Time,'價格',Price,'布林通道下界',LastLower,'空單出場')
                    GO.EndSubscribe()
        
print('全部交易紀錄',OrderRecord.GetTradeRecord())

        
