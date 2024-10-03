# WIP
# Refer
# - https://algotrading101.com/learn/yfinance-guide/

import yfinance as yf
import pandas as pd

import yfinance.utils as yfu
from datetime import date

def ticker():
  stock_id = "0P0000Y61U.HK"
  print("stock:", stock_id )
  stock = yf.Ticker(stock_id)

  # get all stock info
  print("  #info:")
  print(stock.info)

  # get historical market data
  hist = stock.history(period="3mo")
  print("  #history:")
  print(hist)

  # show meta information about the history (requires history() to be called first)
  print("  #history_metadata:")
  print(stock.history_metadata)

  # show actions (dividends, splits, capital gains)
  stock.actions


  print("  #dividends:")
  print(stock.dividends)

  print("  #splits:")
  print(stock.splits)
  print("  #capital_gains:")
  print(stock.capital_gains)  # only for mutual funds & etfs

  # show share count
  print("  #get_shares_full:")
  print(stock.get_shares_full(start="2023-01-01", end=None))

  # show financials:
  print("  #show financials:")
  # - income statement
  print(stock.income_stmt)
  print(stock.quarterly_income_stmt)
  # - balance sheet
  print(stock.balance_sheet)
  print(stock.quarterly_balance_sheet)
  # - cash flow statement
  print(stock.cashflow)
  print(stock.quarterly_cashflow)
  # see `Ticker.get_income_stmt()` for more options

  # show holders
  print("  #show holders:")
  print(stock.major_holders)
  print(stock.institutional_holders)
  print(stock.mutualfund_holders)
  '''
  update@2024-09-19
404 Client Error: Not Found for url: https://query2.finance.yahoo.com/v10/finance/quoteSummary//0P0000Y61U.HK?modules=institutionOwnership%2CfundOwnership%2CmajorDirectHolders%2CmajorHoldersBreakdown%2CinsiderTransactions%2CinsiderHolders%2CnetSharePurchaseActivity&corsDomain=finance.yahoo.com&formatted=false&crumb=SphKHqYvA4B
0P0000Y61U.HK: $0P0000Y61U.HK: possibly delisted; no earnings dates found
  '''

  # Show future and historic earnings dates, returns at most next 4 quarters and last 8 quarters by default.
  # Note: If more are needed use stock.get_earnings_dates(limit=XX) with increased limit argument.
  print("  #earnings_dates:")
  print(stock.earnings_dates)
  '''
  udpate@2024-09-19
  0P0000Y61U.HK: $0P0000Y61U.HK: possibly delisted; no earnings dates found
  '''

  # show ISIN code - *experimental*
  # ISIN = International Securities Identification Number
  print("  #isin:")
  print(stock.isin)

  # show options expirations
  print("  #options:")
  print(stock.options)

  # show news
  print("  #news:")
  print(stock.news)

  # get option chain for specific expiration
  #opt = stock.option_chain('YYYY-MM-DD')
  # data available via: opt.calls, opt.puts

# Example using utils._interval_to_timedelta
def utils_interval_to_timedelta(interval):
  delta = yfu._interval_to_timedelta(interval)
  print("utils_interval_to_timedelta(" + interval + "):" , delta)

  now = date.today()
  print("now:" , now, ", +" + interval+ ":", now + delta)


ticker()
#utils_interval_to_timedelta("1mo")