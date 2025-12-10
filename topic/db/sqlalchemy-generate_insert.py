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
import datetime
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

def df_to_insert_sql(df, table_name):
    """
    Generates a list of SQL INSERT INTO statements from a pandas DataFrame.
    Note: This simplistic method handles basic data types (int, float, string) 
    but does not handle complex data types, SQL injection prevention, 
    or specific database dialect quoting rules as robustly as SQLAlchemy.
    """
    sql_statements = []
    columns = ', '.join(df.columns)
    
    for index, row in df.iterrows():
        # Format values with quotes for strings, no quotes for numbers/NaN becomes NULL
        values = []
        for item in row.values:
            if pd.isna(item):
                values.append('NULL')
            elif isinstance(item, str):
                # Simple escape for single quotes (might need more robust handling)
                nor = item.replace("'", "''")
                values.append(f"'{nor}'")
            elif isinstance(item, datetime.datetime) or isinstance(item, datetime.date):                
               values.append(f"'{str(item)}'")
            else:
                values.append(str(item))
        
        values_str = ', '.join(values)
        statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str})"
        sql_statements.append(statement)
        
    return sql_statements

insert_statements = df_to_insert_sql(df, "cal_tsm_smj_ct")

for statement in insert_statements:
    print(statement)    