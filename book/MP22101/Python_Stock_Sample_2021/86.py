# 載入相關套件
import sys
from screen import GetTAStockDaily
from talib.abstract import SMA,BBANDS,RSI

# 取得要取得的天數
Number = int(sys.argv[1])
# 取得股票代碼
Prod = sys.argv[2]

# 取得N日的股票日資料
Data=GetTAStockDaily(Number,Prod)

# 計算移動平均線
print('SMA',SMA(Data))
# 計算布林通道
print('BBANDS',BBANDS(Data))
# 計算相對強弱指標
print('RSI',RSI(Data))
