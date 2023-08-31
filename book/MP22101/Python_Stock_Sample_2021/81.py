# 載入必要模組
import sys
from screen import GetForeignRank

# 取得排行榜種類
t=sys.argv[1]

# 取得雅虎奇摩外資排行榜
data=GetForeignRank(t)

# 顯示排行榜股票
print(data)

