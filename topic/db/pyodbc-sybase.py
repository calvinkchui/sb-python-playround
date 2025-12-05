import pandas as pd
import pyodbc

import os
from dotenv import load_dotenv
load_dotenv()
dsn = os.environ['test-dsn']
uid = os.environ['test-uid']
pwd = os.environ['test-pwd']

conn = pyodbc.connect("DSN=+ " + dsn + ";UID=" + uid + ";PWD=" + pwd) 

df = pd.read_sql("select top 10 * from dbo.tsm_smj_ct", conn)
print(df.head())


# df.to_excel( "../out/db_pyodbc-sybase-1.xlsx")

