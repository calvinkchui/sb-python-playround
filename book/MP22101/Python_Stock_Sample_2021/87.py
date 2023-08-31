# 載入相關套件
import sys
from screen import GetNumberStockDaily

# 取得股票代碼
Prod = sys.argv[1]

# 取得N日的股票日資料
Data=GetNumberStockDaily(1,Prod)[-1]

DailyTime=Data[0]
DailyHigh=Data[2]
DailyLow=Data[3]
DailyClose=Data[4]

# 計算 Pivot Point
PP=(DailyHigh+DailyLow+DailyClose)/3
R3=DailyHigh+(2*(PP-DailyLow))
R2=PP+DailyHigh-DailyLow
R1=(PP*2)-DailyLow
S1=(PP*2)-DailyHigh
S2=PP-DailyHigh+DailyLow
S3=DailyLow+(2*(DailyHigh-PP))

print(DailyTime,'R3',R3,'R2',R2,'R1',R1,'PP',PP,'S1',S1,'S2',S2,'S3',S3)
