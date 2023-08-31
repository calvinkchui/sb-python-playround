# 載入必要模組
import sys
from screen import GetDealerRank

# 取得排行榜種類
t=sys.argv[1]

# 取得雅虎奇摩自營商排行榜
data=GetDealerRank(t)

# 顯示排行榜股票
print(data)

