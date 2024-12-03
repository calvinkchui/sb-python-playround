import pandas as pd

# see - https://sparkbyexamples.com/pandas/pandas-read-excel-with-examples/
# install dpendency if required - `pip install openpyxl`

'''
pf.read_excel( file ,
    sheet_name = ?, # by name e.g. "name", by index e.g. 0
    index_col = ?, # 0 - by first column
    header = ?, # 0 - 0 by first row, None
    usecols = [0,2] - get column 0 & 2 only



# get data size by .shape
e.g.
> df.shape
(4,4)

# get data info by info()
e.g.
> df.info()
<Class 
...
Column 1      4 non-null object
Column 2      4 non-null int64
....
'''


# Read Excel file
df = pd.read_excel('assets/programmingLang.xlsx')
print(df)

'''
     Language  Front-end Web  Back-End Web  Mobile  Desktop
0  Javascript            1.0           1.0     4.0      NaN
1  TypeScript            3.0           NaN     NaN      NaN
2       Scala            NaN           2.0     NaN      1.0
3      Python            NaN           3.0     NaN      3.0
4        Java            NaN           NaN     2.0      NaN
'''

# Ignore Column Name
columns = ['languange','fron_end','back_end','mobile', 'desktop']
df2 = pd.read_excel('assets/programmingLang.xlsx', 
                   header=0, names = columns)
print(df2)

'''
    languange  fron_end  back_end  mobile  desktop
0  Javascript       1.0       1.0     4.0      NaN
1  TypeScript       3.0       NaN     NaN      NaN
2       Scala       NaN       2.0     NaN      1.0
3      Python       NaN       3.0     NaN      3.0
4        Java       NaN       NaN     2.0      NaN
'''


