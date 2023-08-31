# 載入必要模組
import sys
from screen import GetMarginTrade

# 取得日期以及股票群組
date=sys.argv[1]
group=sys.argv[2]

# 取得股票融資融券交易資訊
data=GetMarginTrade(date,group)

# 依照成交金額進行資料排序
data.sort(key=lambda x:int(x[6])-int(x[5])  , reverse=True)

# 顯示前10名當日融資增加最大值
print(data[:10])
