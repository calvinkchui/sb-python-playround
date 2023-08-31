# 載入相關套件
import sys,haohaninfo 
from screen import GetNumberStockDaily

# 選擇報價平台
Broker = sys.argv[1]
# 定義商品名稱
Prod = sys.argv[2]

# 取得前一日收盤價資訊
LastDayInfo=GetNumberStockDaily(1,Prod)[-1]
DailyHigh=LastDayInfo[2]
DailyLow=LastDayInfo[3]
DailyClose=LastDayInfo[4]

# 計算 CDP
CDP=(DailyHigh+DailyLow+DailyClose)/3
AH=CDP+DailyHigh-DailyLow
NH=2*CDP-DailyLow
NL=2*CDP-DailyHigh
AL=CDP-DailyHigh+DailyLow
print('NH',NH,'NL',NL)

# 訂閱報價
GO = haohaninfo.GOrder.GOQuote()
for row in GO.Subscribe( Broker, 'match', Prod ):
    # 取得價格欄位
    Price=float(row[2])
    # 突破壓力支撐價位
    if Price > NH:
        print('當前價',Price,'突破壓力價位',NH,'，代表可能反轉或有趨勢發生')
        GO.EndSubscribe()
    elif Price < NL:
        print('當前價',Price,'突破支撐價位',NL,'，代表可能反轉或有趨勢發生')
        GO.EndSubscribe()
