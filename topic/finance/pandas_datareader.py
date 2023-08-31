'''
https://pandas-datareader.readthedocs.io/en/latest/


WIP  
'''


import pandas_datareader.data as web
import pandas as pd
import datetime as dt

#df = web.DataReader('GE', 'yahoo', start='2022-09-10', end='2022-10-09')
#df.head()

#start_date = "2020-01-1"
#end_date = "2020-12-31"
#data = web.DataReader(name="TSLA", data_source='yahoo', start=start_date, end=end_date)
#print(data)


# ------------------------------------------------------------
#FRED
# ------------------------------------------------------------

start = dt.datetime(2020, 1, 1)
end = dt.datetime(2023, 1, 27)

gdp = web.DataReader('GDP', 'fred', start, end)
print(gdp.loc['2023-01-01'])

inflation = web.DataReader(['CPIAUCSL', 'CPILFESL'], 'fred', start, end)
print(inflation.head)

'''
<bound method NDFrame.head of             CPIAUCSL  CPILFESL
DATE
2020-01-01   259.037   266.626
2020-02-01   259.248   267.283
2020-03-01   258.124   267.090
2020-04-01   256.092   265.771
2020-05-01   255.868   265.574
2020-06-01   256.986   265.952
'''
