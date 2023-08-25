'''
Python for Finance Part 2: Simple Moving Average
  https://www.linkedin.com/pulse/python-finance-part-2-simple-moving-average-henry-meier
  
- use yfinance_cache  
- use MyTT

https://github.com/mpquant/Python-Financial-Technical-Indicators-Pandas
'''

#import yfinance as yf
import yfinance_cache as yfc
import matplotlib.pyplot as plt
#from topic.finance.MyTT import *

# Input the start and end dates and the stock ticker symbol
start_date = input("Enter the start date (YYYY-MM-DD): ")
end_date = input("Enter the end date (YYYY-MM-DD): ")
symbol = input("Enter the stock ticker symbol: ")

start_date = start_date or "2022-01-01"
end_date = end_date or "2023-07-31"
symbol = symbol or "0005.HK"

n_short=15
n_long=50

# Download the stock price data from Yahoo Finance API
#data = yf.download(symbol, start=start_date, end=end_date)
src = yfc.Ticker(symbol);
data = src.history(start=start_date, end=end_date)

# Calculate the short-term and long-term Simple Moving Averages (SMAs)
sma_short = data['Close'].rolling(window=n_short).mean()
sma_long = data['Close'].rolling(window=n_long).mean()
#sma_short = MA(data['Close'],n_short)
#xsma_long = MA(data['Close'],n_long)

# Determine the Buy or Sell signals based on the SMA crossovers
signals = [None]*len(sma_short)
for i in range(1, len(sma_short)):
    if sma_short[i] > sma_long[i] and sma_short[i-1] <= sma_long[i-1]:
        signals[i] = 'Buy'
        print(f"Buy signal detected on {data.index[i].date()}")
    elif sma_short[i] < sma_long[i] and sma_short[i-1] >= sma_long[i-1]:
        signals[i] = 'Sell'
        print(f"Sell signal detected on {data.index[i].date()}")
        
        
                
        
# Add the signals to the data frame
data['Signal'] = signals


plt.figure(figsize=(10,6))

# Plot the stock price and SMAs, and add markers for the signal changes
plt.plot(data['Close'], label='Price')
plt.plot(sma_short, label= str(n_short) +'-day SMA')
plt.plot(sma_long, label= str(n_long) + '-day SMA')
buy_points = data[data['Signal'] == 'Buy']
sell_points = data[data['Signal'] == 'Sell']
plt.plot(buy_points.index, buy_points['Close'], '^', markersize=10, color='g', label='Buy signal')
plt.plot(sell_points.index, sell_points['Close'], 'v', markersize=10, color='r', label='Sell signal')

# Add the legend and title to the plot
plt.legend()
plt.title(f'{symbol} Stock Price ({start_date} to {end_date})')




# Save the plot as an image
plt.show()
#plt.savefig("out/yf_analysis_plot.png")        