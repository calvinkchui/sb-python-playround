# 載入相關套件
import sys
from screen import GetNumberStockDaily

# 取得要取得的天數
Number = int(sys.argv[1])
# 取得股票代碼
Prod = sys.argv[2]

# 取得N日的股票日資料
Data=GetNumberStockDaily(Number,Prod)
print(Data)