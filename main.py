import sys

#https://www.tutorialspoint.com/python/index.htm

# Hello World
print("run 'main.py'")

target = "yfinance"  #default
if len(sys.argv) > 1:
  target = sys.argv[1]

if target == 'demo':
  # ----------------------------------------------
  # Basic
  # ----------------------------------------------

  #import basic.var as var

  # Function
  #import basic.function as fx
  #import basic.function_mapFilterReduce as fxMapRfilterReduce
  #fxMapRfilterReduce.demo()
  #import basic.pyjson as pyjson
  #import basic.io as io

  # ----------------------------------------------
  # Advance
  # ----------------------------------------------

  #log
  #import advance.log as log
  import advance.decorator as d
  d.demo()
  
  # ----------------------------------------------
  # Topic - Data
  # ----------------------------------------------
  #import topic.data.pandas_01_basic

# ----------------------------------------------
# Topic - Finance
# ----------------------------------------------
#import Topic.finance.alpha_vantage
if target == "yfinance":
  import topic.finance.yfinance

#import topic.finance.yfinance_cache

# MyTT https://github.com/mpquant/Python-Financial-Technical-Indicators-Pandas
#import topic.finance.MyTTSample

# finance plot
#import topic.finance.mplfinance

if target == "pandas_datareader":
  import topic.finance.pandas_datareader

if target == "yfinance_analysis":
  import topic.finance.yfinance_analysis_01
