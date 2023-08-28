# https://github.com/mpquant/Python-Financial-Technical-Indicators-Pandas/blob/main/MyTT.py

import yfinance_cache as yfc
import matplotlib.pyplot as plt

from topic.finance.MyTT import *

start_date = "2023-01-01"
end_date = "2023-01-31"
symbol = "0005.HK"

src = yfc.Ticker(symbol);
data = src.history(start=start_date, end=end_date)

print(symbol + ":")
print(type(data)) #pandas.core.frame.DataFrame
print(data)

idx = data['Close'].rolling(window=5).mean()
print("SMA5 (.rolling):") 
print(type(idx))
print(idx)

idx = MA(data['Close'],5)
print("SMA5 (MA):")
print(type(idx)) # pandas.core.series.Series
print(idx)


ma5 = MA(data['Close'],5)
print("SMA5 (.index):")
print(type(data['Close'].index))
print(data['Close'].index)

print("SMA5 (rebuild):")
print(type(ma5))
print( pd.Series(ma5, index=data['Close'].index) )
