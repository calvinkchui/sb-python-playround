# https://pythonviz.com/pandas/pandas-series-map-dataframe-applymap/

import numpy as np
import pandas as pd

# -----------------------------------------------------------
def demo01_series_op():
    height = pd.Series([1.67, 1.78, 1.45, 1.20])

    print("Demo 1 - Series Operator:")
    print(height * 100)
    print(height > 1.5)
'''    
Demo 1 - Series Operator:
0    167.0
1    178.0
2    145.0
3    120.0
dtype: float64
0     True
1     True
2    False
3    False
dtype: bool
'''

# -----------------------------------------------------------
def demo01_series_map():

    countries_visited = pd.Series(['Canada', 'Canada', 'Japan', 'Japan', 'Japan', 'Taiwan', 'Taiwan', 'United Kingdom'])
    mapped = countries_visited.map({
      'Canada': 'Americas', 
      'Japan': 'Asia', 
      'Taiwan': 'Asia', 
      'United Kingdom': 'Europe'})    
    print("Demo 2a - Series.map:")
    print ( mapped )

    print ( "Demo 2b - Series.value_counts()" )
    print ( mapped.value_counts() )
'''
Demo 2 - Series.map:
0    Americas
1    Americas
2        Asia
3        Asia
4        Asia
5        Asia
6        Asia
7      Europe

Demo 2b - Series.value_counts()
Asia        5
Americas    2
Europe      1
Name: count, dtype: int64
'''


# -----------------------------------------------------------
def demo01_df_applymap():


  measures = pd.DataFrame({'height': [1.3,0.6],'width': [0.8,0.9],'depth':[2.5,1.5]})
  rst = measures.applymap(lambda x: x * 100)
  print ( "Demo 3 - Dataframe.applymap()" )
  print ( rst )
'''
Demo 3 - Dataframe.applymap()
   height  width  depth
0   130.0   80.0  250.0
1    60.0   90.0  150.0
'''

# -----------------------------------------------------------
demo01_series_op()
demo01_series_map()

demo01_df_applymap()