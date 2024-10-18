import numpy as np
import pandas as pd

'''
see also concat
e.g. result = pd.concat([result, stock_df], axis=1)
'''

df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})

#1 Join by index
print ("#1 join by index ")
print (df.join(other, lsuffix='_caller', rsuffix='_other'))
'''
#1 join   
  key_caller   A key_other    B
0         K0  A0        K0   B0     
1         K1  A1        K1   B1     
2         K2  A2        K2   B2     
3         K3  A3       NaN  NaN     
4         K4  A4       NaN  NaN     
5         K5  A5       NaN  NaN  
'''


print ("#2 join by key coluumn ")
print (df.set_index('key').join(other.set_index('key')))
'''
#2 join by key coluumn
      A    B
key
K0   A0   B0
K1   A1   B1
K2   A2   B2
K3   A3  NaN
K4   A4  NaN
K5   A5  NaN
'''


print ("#3 join on ")
print (df.join(other.set_index('key'), on='key'))
'''
#3 join on
  key   A    B
0  K0  A0   B0
1  K1  A1   B1
2  K2  A2   B2
3  K3  A3  NaN
4  K4  A4  NaN
5  K5  A5  NaN
'''


# https://stackoverflow.com/questions/32277473/merge-two-dataframes-based-on-multiple-keys-in-pandas
print("#4 Join with multiple keys (1-1)")
a = pd.DataFrame({'A':['0', '0', '1','1'],'B':['0', '1', '0','1'], 'v':[True, False, False, True]})
b = pd.DataFrame({'A':['0', '0', '1','1'], 'B':['0', '1', '0','1'],'v':[False, True, True, True]})

result = pd.merge(a, b, on=['A','B'], how='inner', suffixes=['_and', '_or'])
print(result)
'''
   A  B  v_and   v_or
0  0  0   True  False
1  0  1  False   True
2  1  0  False   True
3  1  1   True   True
'''

print("#4 Join with multiple keys (1-n)")
c = pd.DataFrame({'A':['0', '0', '1','1'], 'B':['0', '1', '1','1'],'x':['0-0', '0-1', '1-1 A', '1-1 B']})
result = pd.merge(a, c, on=['A','B'], how='left', suffixes=['_and', '_or'])
print(result)

'''
   A  B      v      x
0  0  0   True    0-0
1  0  1  False    0-1
2  1  0  False    NaN
3  1  1   True  1-1 A
4  1  1   True  1-1 B
'''
