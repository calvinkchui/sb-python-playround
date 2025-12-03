import pandas as pd
import pyodbc

import os
from dotenv import load_dotenv
load_dotenv()
uid = os.environ['rhine-uid']
pwd = os.environ['rhine-pwd']

conn = pyodbc.connect("DSN=rhine;UID=" + uid + ";PWD=" + pwd) 

df = pd.read_sql("select top 10 * from dbo.rc_student", conn)
print(df.head())