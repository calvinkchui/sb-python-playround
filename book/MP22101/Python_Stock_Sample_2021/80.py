# 載入必要模組
import sys
from screen import GetHotRank

# 取得排行榜種類、交易所、資料數量
t=sys.argv[1]
e=sys.argv[2]
n=sys.argv[3]

# 取得雅虎奇摩排行榜
data=GetHotRank(t,e,n)

# 顯示排行榜股票
print(data)

