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

  import basic.string as str
  str.demo()

  #import basic.var as var
  #var.demo()
  #var.moreDemo()

  #import basic.zipunzip as zz
  #zz.demo()

  # ----------------------------------------------
  # Advance
  # ----------------------------------------------

  #log
  #import advance.log as log
  #import advance.decorator as d
  #d.demo()

  # ----------------------------------------------
  # Topic - Data
  # ----------------------------------------------
  #import topic.data.pandas_01_basic

if target == "pandas":
  import topic.data.pandas_0010_basic
  #import topic.data.pandas_0100_readCsv 
   

# ----------------------------------------------
# Topic - Finance
# ----------------------------------------------
#import Topic.finance.alpha_vantage
if target == "yfinance":
  import topic.finance.yfinance

#impor tot topic.finance.yfinance_cache

# MyTT https://github.com/mpquant/Python-Financial-Technical-Indicators-Pandas
#import topic.finance.MyTTSample

# finance plot
#import topic.finance.mplfinance

if target == "pandas_datareader":
  import topic.finance.pandas_datareader

if target == "yfinance_analysis":
  import topic.finance.yfinance_analysis_01



# ----------------------------------------------
# Topic - Rich-text
# ----------------------------------------------
if target == "rich": 
  import topic.rich_text.rich

# ----------------------------------------------
if target == "rich_prompt": 
  import topic.rich_text.rich_prompt  
