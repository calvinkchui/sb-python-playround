'''
https://pypi.org/project/yfinance-cache/


* Path
  * Window=C:/Users/<USER>/AppData/Local/py-yfinance-cache
  * Linux=/home/<USER>/.cache/py-yfinance-cache
  

'''
import yfinance_cache as yfc

msft = yfc.Ticker("DIS")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="1d")

hist = msft.history(period="5d")

# etc. See yfinance documentation for full API