'''
setup:
```sh
pip install sqlalchemy-sybase
```

```sql
select * into cal_tsm_smj_ct from tsm_smj_ct

alter table cal_tsm_smj_ct 
 add constraint PK_CAL_TSM_SMJ_CT PRIMARY KEY (smj_code)
```

'''
from sqlalchemy import create_engine
import pandas as pd
import pyodbc

import os
from dotenv import load_dotenv
load_dotenv()


uid = os.environ['test-uid']
pwd = os.environ['test-pwd']
dsn = os.environ['test-dsn']

conn = f"sybase+pyodbc://{uid}:{pwd}@{dsn}";
#print(conn)
engine = create_engine(conn, echo=True) # dump SQL if echo=True

#conn = pyodbc.connect("DSN=+ " + dsn + ";UID=" + uid + ";PWD=" + pwd) 

df = pd.read_sql("select top 10 * from dbo.tsm_smj_ct", engine)
print(df.head())

#print("export to excel")
#df.to_excel( "../../out/db_pyodbc-sybase-1.xlsx")

df = df.drop(columns=['timestamp'])

print("export to db")
n = df.to_sql( "cal_tsm_smj_ct", engine, 
   if_exists="append", index=False
   )
print(f"  export: {n} rows")

