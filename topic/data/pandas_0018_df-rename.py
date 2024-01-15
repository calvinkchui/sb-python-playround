import numpy as np
import pandas as pd


df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'X': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5'],
                   'Y': ['B0', 'B1', 'B2', 'B3', 'B4', 'B5']})

df.rename(columns={
    'X': 'A', 
    'Y': 'B'
})

print(df)