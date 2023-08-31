# 載入必要模組
import sys
from screen import GetStockAfterHour

# 取得日期以及股票群組
date=sys.argv[1]
group=sys.argv[2]

# 取得股票盤後定價交易資訊
data=GetStockAfterHour(date,group)

# 依照成交金額進行資料排序
data.sort(key=lambda x:int(x[4])  , reverse=True)

# 顯示前10名盤後定價交易最大金額
print(data[:10])
