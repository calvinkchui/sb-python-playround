#載入相關套件及函數
import sys,datetime
import matplotlib.pyplot as plt
from history_function import getHistoryTick

#將日期以及股票代碼變成參數帶入
date=sys.argv[1]
stockid=sys.argv[2]

#取得成交資訊
Data = getHistoryTick('simulator_stock',date,stockid,'match')
#取得轉換時間字串至時間格式
Time = [ datetime.datetime.strptime(line[0],"%Y/%m/%d %H:%M:%S.%f") for line in Data ]
#價格由字串轉數值
Price = [ float(line[2]) for line in Data ]

#定義圖表物件       
ax = plt.subplot(111)

#繪製圖案 plot_date(X軸物件, Y軸物件, 線風格)
ax.plot_date(Time, Price, 'k-')

#定義title
plt.title('Stock '+stockid+' Price Line')

#顯示繪製圖表
plt.show()
