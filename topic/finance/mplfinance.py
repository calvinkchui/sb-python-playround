# pip install --upgrade mplfinance

import yfinance_cache as yfc
import mplfinance as mpf

from topic.finance.MyTT import *

start_date = "2023-01-01"
end_date = "2023-01-31"
symbol = "0005.HK"

src = yfc.Ticker(symbol);
data = src.history(start=start_date, end=end_date)


# Sample Plot
#mpf.plot(data,type='candle',volume=True)

# Adding plots to the basic mplfinance plot()
# https://github.com/matplotlib/mplfinance/blob/master/examples/addplot.ipynb


idx = data['Close'].index;

r_ma5 = MA(data['Close'],5)
s_ma5=pd.Series( r_ma5, index=idx)
df_ma5=pd.DataFrame(data=s_ma5, index=idx)

ma5 = mpf.make_addplot(df_ma5)
mpf.plot(data,volume=True,addplot=ma5)