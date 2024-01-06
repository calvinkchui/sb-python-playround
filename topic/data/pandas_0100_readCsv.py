import pandas as pd

# see - https://sparkbyexamples.com/pandas/pandas-read-excel-with-examples/
# install dpendency if required - `pip install openpyxl`

# Read Excel file
df = pd.read_csv('assets/data-pandas100.csv',
                 parse_dates=['dob'])
print(df)

print(df.info())