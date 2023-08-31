# 載入必要模組
import sys
from screen import GetThreeMajor

# 取得日期
date=sys.argv[1]

# 取得外資彙總表交易資訊
# 若要取得自營商、投信則改type參數即可
data=GetThreeMajor(date,1)

# 依照成交金額進行資料排序
data.sort(key=lambda x:int(x[11]) , reverse=True)

# 顯示前10名當日外資買超最大值
print(data[:10])

