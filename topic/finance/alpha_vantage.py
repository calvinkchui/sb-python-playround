# Import TimeSeries class 
from alpha_vantage.timeseries import TimeSeries 
from pprint import pprint
import os
#import pandas
'''
https://www.quora.com/How-do-I-get-free-daily-stock-data-in-Python-for-free-with-30-stocks
'''

ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

# This is to prompt you to change the Quandl Key 
if ALPHA_VANTAGE_API_KEY == 'REPLACE-THIS-TEXT-WITH-A-REAL-API-KEY': 
    raise Exception("Please provide a valid Alpha Vantage API key!") 

# Functions
def demo():
    getData()
    
def getData(): 
     
     
    # Initialize the TimeSeries class with key and output format 
    ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas') 
     
    # Get json object with the intraday data and information of the data 
    intraday_data, data_info = ts.get_intraday( 
        'GOOGL', outputsize='full', interval='1min') 
     
    # Print the information of the data 
    print(data_info)
    # {'1. Information': 'Intraday (1min) open, high, low, close prices and volume', '2. Symbol': 'GOOGL', '3. Last Refreshed': '2023-08-23 19:59:00', '4. Interval': '1min', '5. Output Size': 'Full size', '6. Time Zone': 'US/Eastern'}

    # Print the intraday data 
    pprint(intraday_data.head(2)) 
'''
                     1. open  2. high  3. low  4. close  5. volume
date
2023-08-23 19:59:00   133.83   133.93  133.69    133.70     1985.0
2023-08-23 19:58:00   133.80   133.80  133.68    133.79     1452.0
'''

demo()