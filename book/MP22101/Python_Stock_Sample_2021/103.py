# 載入相關套件
import sys,haohaninfo,datetime 
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
# 定義爆量口數
BigOrder=1000

# 訂閱報價
GO = haohaninfo.GOrder.GOQuote()
# 進場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    Qty=float(row[3])
    ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
    # 每分鐘判斷一次爆量
    if ChangeKFlag==1:
        # 判斷是否爆量
        Volume=KBar1M.GetVolume()
        if len(Volume) >= 2:
            LastVolume = Volume[-2]
            if LastVolume > BigOrder:
                # 判斷收盤價是否高於開盤價            
                LastClose=KBar1M.GetClose()[-2]
                LastOpen=KBar1M.GetOpen()[-2]
                if LastClose > LastOpen:
                    OrderRecord.Order('B',Prod,Time,Price,1)
                    print(Time,'爆量',LastVolume,'多單進場')
                    GO.EndSubscribe()
                elif LastClose < LastOpen:
                    OrderRecord.Order('S',Prod,Time,Price,1)
                    print(Time,'爆量',LastVolume,'空單進場')
                    GO.EndSubscribe()
        
# 出場判斷
for row in GO.Subscribe( Broker, 'match', Prod ):    
    # 取得時間、價格欄位
    Time=datetime.datetime.strptime(row[0],'%Y/%m/%d %H:%M:%S.%f')
    Price=float(row[2])
    Qty=float(row[3])
    ChangeKFlag=KBar1M.AddPrice(Time,Price,Qty)
    # 每分鐘判斷一次爆量
    if ChangeKFlag==1:
        # 判斷是否爆量
        Volume=KBar1M.GetVolume()[-2]
        if Volume > BigOrder:
            if OrderRecord.GetOpenInterest() == 1:
                # 多單出場
                OrderRecord.Cover('S',Prod,Time,Price,1)
                print(Time,'爆量',Volume,'多單出場')
                GO.EndSubscribe()       
            if OrderRecord.GetOpenInterest() == -1:
                # 空單出場
                OrderRecord.Cover('B',Prod,Time,Price,1)
                print(Time,'爆量',Volume,'空單出場')
                GO.EndSubscribe()      
            
print('全部交易紀錄',OrderRecord.GetTradeRecord()) 
