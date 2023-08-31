# 載入相關套件及函數
import sys
from history_function import getHistoryTick

# 將股票代碼變成參數帶入
broker=sys.argv[1]
date=sys.argv[2]
stockid=sys.argv[3]
stoplossratio=float(sys.argv[4])

# 取得成交資訊
Data = getHistoryTick(broker,date,stockid,'match')

# 取得進場時間以及價格
OrderTime=Data[0][0]
OrderPrice=float(Data[0][2])

# 判斷停損 或是 收盤出場
for rnum in range(1,len(Data)):
    Price=float(Data[rnum][2])
    # 停損判斷
    if Price <= OrderPrice * (1-stoplossratio):
        CoverTime=Data[rnum][0]
        CoverPrice=float(Data[rnum][2])
        # 計算績效
        Profit=round(CoverPrice-OrderPrice,3)
        break
    # 收盤出場
    elif rnum == len(Data) -1:
        CoverTime=Data[rnum][0]
        CoverPrice=float(Data[rnum][2])
        # 計算績效
        Profit=round(CoverPrice-OrderPrice,3)

print(date,stockid,'Buy OrderTime',OrderTime,'OrderPrice',OrderPrice,'CoverTime',CoverTime,'CoverPrice',CoverPrice,'Profit',Profit)
