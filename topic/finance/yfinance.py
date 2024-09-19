# WIP
# Refer
# - https://algotrading101.com/learn/yfinance-guide/

import yfinance as yf
import pandas as pd

import yfinance.utils as yfu
from datetime import date

def ticker():
  msft = yf.Ticker("0P0000Y61U.HK")

  # get all stock info
  msft.info

  # get historical market data
  hist = msft.history(period="3mo")
  print("history:")
  print(hist)

  # show meta information about the history (requires history() to be called first)
  msft.history_metadata

  # show actions (dividends, splits, capital gains)
  msft.actions

 
  print("dividends:")
  print(msft.dividends)

  print("splits:")
  msft.splits
  msft.capital_gains  # only for mutual funds & etfs

  # show share count
  print("get_shares_full:")
  msft.get_shares_full(start="2023-01-01", end=None)

  # show financials:
  print("show financials:")
  # - income statement
  msft.income_stmt
  msft.quarterly_income_stmt
  # - balance sheet
  msft.balance_sheet
  msft.quarterly_balance_sheet
  # - cash flow statement
  msft.cashflow
  msft.quarterly_cashflow
  # see `Ticker.get_income_stmt()` for more options

  # show holders
  print("show holders:")
  msft.major_holders
  msft.institutional_holders
  msft.mutualfund_holders
  '''
  update@2024-09-19
404 Client Error: Not Found for url: https://query2.finance.yahoo.com/v10/finance/quoteSummary//0P0000Y61U.HK?modules=institutionOwnership%2CfundOwnership%2CmajorDirectHolders%2CmajorHoldersBreakdown%2CinsiderTransactions%2CinsiderHolders%2CnetSharePurchaseActivity&corsDomain=finance.yahoo.com&formatted=false&crumb=SphKHqYvA4B
0P0000Y61U.HK: $0P0000Y61U.HK: possibly delisted; no earnings dates found
  '''

  # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
  # Note: If more are needed use msft.get_earnings_dates(limit=XX) with increased limit argument.
  print("earnings_dates:")
  msft.earnings_dates
  '''
  udpate@2024-09-19
  0P0000Y61U.HK: $0P0000Y61U.HK: possibly delisted; no earnings dates found
  '''

  # show ISIN code - *experimental*
  # ISIN = International Securities Identification Number
  print("isin:")
  msft.isin

  # show options expirations
  print("options:")
  msft.options

  # show news
  print("news:")
  msft.news

  # get option chain for specific expiration
  #opt = msft.option_chain('YYYY-MM-DD')
  # data available via: opt.calls, opt.puts

# Example using utils._interval_to_timedelta
def utils_interval_to_timedelta(interval):
  delta = yfu._interval_to_timedelta(interval)
  print("utils_interval_to_timedelta(" + interval + "):" , delta)

  now = date.today()
  print("now:" , now, ", +" + interval+ ":", now + delta)


#ticker()
utils_interval_to_timedelta("1mo")