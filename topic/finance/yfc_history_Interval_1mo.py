import datetime

import yfinance as yf
import yfinance_cache as yfc
import matplotlib.pyplot as plt


import pandas as pd



src = yfc.Ticker("0005.HK")


# Case 1
'''
ed = datetime.datetime.now()
print ("end time:", ed, type(ed))
sd = datetime.datetime(2014, 1, 1, 0, 0, 0, 1)
print ("start time:", sd, type(sd))
data = src.history(start=sd,end=ed, interval="1mo") #  'start' must be datetime not <class 'datetime.date'> for interval 1mo
'''


# Case 2
#data = src.history(period="1y", interval="1mo")
# if yfcd.intervalToTimedelta[interval] <= timedelta(days=1):
#   TypeError: '<=' not supported between instances of 'relativedelta' and 'datetime.timedelta'

#data = src.history(period="max", interval="1mo")



# Case 3
'''
symbol = "AAPL"
start = "2024-01-01"
end = "2024-02-01"
data = yfc.download(symbol, start, end, interval="1mo")
'''

#
data = src.history(period="1y")
#print(data)

# https://www.qmr.ai/yfinance-library-the-definitive-guide/
df_new = data.groupby(pd.Grouper(freq='MS')).agg({"Open": "first", 
                                             "High": "max", 
                                             "Low": "min", 
                                             "Close": "last",
                                             "Volume": "sum"})

print (df_new)
