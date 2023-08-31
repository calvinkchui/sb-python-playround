# 載入相關套件及函數
import sys
from history_function import getHistoryTick

# 將股票代碼變成參數帶入
broker=sys.argv[1]
date=sys.argv[2]
stockid=sys.argv[3]
gapratio=float(sys.argv[4])
stoplossratio=float(sys.argv[5])
takeprofitratio=float(sys.argv[6])

# 取得成交資訊
Data = getHistoryTick(broker,date,stockid,'match')

# 取得開盤價
OpenPrice=float(Data[0][2])

# 定義初始部位
Index=0

# 策略判斷
for rnum in range(1,len(Data)):
    Time=Data[rnum][0]
    Price=float(Data[rnum][2])
    # 進場判斷
    if Index == 0:
        # 多單進場判斷
        if Price >= OpenPrice * (1+gapratio) :
            Index=1
            OrderTime=Time
            OrderPrice=Price
        # 空單進場判斷
        elif Price <= OpenPrice * (1-gapratio) :
            Index=-1
            OrderTime=Time
            OrderPrice=Price
    # 多單出場判斷
    if Index == 1:
        # 停利判斷
        if Price >= OrderPrice * (1+takeprofitratio):
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(CoverPrice-OrderPrice,3)
            print(date,stockid,'Buy OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
            break
        # 停損判斷
        if Price <= OrderPrice * (1-stoplossratio):
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(CoverPrice-OrderPrice,3)
            print(date,stockid,'Buy OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
            break
        # 收盤出場
        elif rnum == len(Data) -1:
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(CoverPrice-OrderPrice,3)
            print(date,stockid,'Buy OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
    # 空單出場判斷
    if Index == -1:
        # 停利判斷
        if Price <= OrderPrice * (1-takeprofitratio):
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(OrderPrice-CoverPrice,3)
            print(date,stockid,'Sell OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
            break
        # 停損判斷
        if Price >= OrderPrice * (1+stoplossratio):
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(OrderPrice-CoverPrice,3)
            print(date,stockid,'Sell OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
            break
        # 收盤出場
        elif rnum == len(Data) -1:
            CoverTime=Data[rnum][0]
            CoverPrice=float(Data[rnum][2])
            # 計算績效
            Profit=round(OrderPrice-CoverPrice,3)
            print(date,stockid,'Sell OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)



