# 載入必要模組
import sys
from screen import GetCraditTrade

# 取得日期
date=sys.argv[1]

# 取得股票融券借券交易資訊
data=GetCraditTrade(date)

# 依照成交金額進行資料排序
data.sort(key=lambda x:int(x[12]) , reverse=True)

# 顯示前10名當日借券最大值
print(data[:10])

