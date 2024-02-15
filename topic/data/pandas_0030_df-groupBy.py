#https://www.w3schools.com/python/pandas/ref_df_groupby.asp
#https://pythonviz.com/pandas/pandas-groupby-tutorial/
import pandas as pd
import numpy as np

data_co2 = {
  'co2': [95, 90, 99, 104, 105, 94, 99, 104],
  'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
  'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

def demo1():
    df = pd.DataFrame(data_co2)
    print(df.groupby(by=["car"]).mean( ["co2"]))
'''
        co2
car         
Ford   100.5
Skoda   97.0
'''

def demo2_agg():
    df = pd.DataFrame(data_co2)
    print(df.groupby(by=["car"]).agg( 
        {'co2': np.mean})
    )

def demo2_agg_join(): # .join
    df = pd.DataFrame(data_co2)
    print(df.groupby(by=["car"]).agg( 
        {'model': ','.join })
    )
'''
                            model
car                              
Ford    Fiesta,Focus,Mondeo,B-Max
Skoda  Citigo,Fabia,Rapid,Octavia
'''

def demo4_newColumn():
    df = pd.DataFrame(data_co2)
    print(df.groupby(by=["car"]).agg( 
        co2_mean=('co2', np.mean),
        co2_max=('co2', np.max)
    ))
'''    
       co2_mean  co2_max
car                     
Ford      100.5      105
Skoda      97.0      104
'''



# -------------------------------------------------------

demo1()
demo2_agg()
demo2_agg_join()
demo4_newColumn()