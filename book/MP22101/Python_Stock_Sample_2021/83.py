# 載入必要模組
from screen import GetWeightedStock

# 取得權值股
data=GetWeightedStock()

# 顯示權值股股票
print(data[:100])

