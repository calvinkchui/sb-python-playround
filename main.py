import sys

#https://www.tutorialspoint.com/python/index.htm

# Hello World

target = "yfinance"  #default
if len(sys.argv) > 1:
  target = sys.argv[1]

print("run 'main.py'", target)


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

  #import basic.string as str
  #str.demo()

  #import basic.var as var
  #var.demo()
  #var.moreDemo()

  #import basic.zipunzip as zz
  #zz.demo()

  import basic.one_liners as ol
  ol.demo()

if target == 'singleton':
  import basic.singleton

# ----------------------------------------------
# Advance
# ---------------------------------------------

if target == "log":    
  import advance.log as log
  log.demo()

if target == "decorator":   
  import advance.decorator as d
  d.demo()

  # ----------------------------------------------
  # Topic - Data
  # ----------------------------------------------
  #import topic.data.pandas_01_basic

if target == "pandas":
  #import topic.data.pandas_0010_basic
  #import topic.data.pandas_0100_readCsv 
  #import topic.data.pandas_0018_df_xarray
  #import topic.data.pandas_0090_multiindex
  import topic.data.pandas_0100_df_to_nestjson
  
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
