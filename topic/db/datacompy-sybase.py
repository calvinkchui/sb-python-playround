'''
setup:
```sh
pip install sqlalchemy-sybase datacompy
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
from datacompy.core import Compare

import os
from dotenv import load_dotenv
load_dotenv()


uid = os.environ['test-uid']
pwd = os.environ['test-pwd']
dsn = os.environ['test-dsn']

table_fr = 'tsm_smj_ct'
table_to = 'cal_tsm_smj_ct'
join_keys = ['smj_code']

def compare_db_tables_datacompy(table_fr, table_to, engine_fr, engine_to, join_columns):
   """
   Connects to a database, loads two tables into pandas DataFrames,
   and compares them using the datacompy library.
   """


   dfFr = pd.read_sql(f"select * from {table_fr}", engine_fr)
   dfTo = pd.read_sql(f"select * from {table_to}", engine_to)

   # --- DataComPy Comparison ---
   compare = Compare(
      dfFr,
      dfTo,
      join_columns=join_columns, # Column(s) to join on
      abs_tol=0.0001,             # Tolerance for floating point comparisons
      df1_name=table_fr,           # Optional names for clarity in report
      df2_name=table_to
   )

   # Print a human-readable summary report
   if compare.matches():
      print("\n--- Comparison Result: DataFrames match exactly ---")
   else:
      print("\n--- Comparison Result: Differences Found ---")
      # The report() method generates a detailed summary
      print(compare.report())

   # You can access specific differing rows/columns if needed
      if not compare.df1_unq_rows.empty:
         print(f"\n--- Rows unique to {table_name_1} ---")
         print(compare.df1_unq_rows)
        
      if not compare.df2_unq_rows.empty:
         print(f"\n--- Rows unique to {table_name_2} ---")
         print(compare.df2_unq_rows)


try:
   connFr = f"sybase+pyodbc://{uid}:{pwd}@{dsn}";
   #print(conn)
   engineFr = create_engine(connFr, echo=True) # dump SQL if echo=True
   engineTo = engineFr
   
   compare_db_tables_datacompy(table_fr, table_to, engineFr, engineTo, join_keys)

except Exception as e:
   print(f"An unexpected error occurred: {e}")
finally:
   print("\nDatabase connection closed.")

'''

--- Comparison Result: Differences Found ---
DataComPy Comparison
-------------------

DataFrame Summary
-----------------

DataFrame  Columns  Rows
------------------------
tsm_smj_ct        9    10
cal_tsm_smj_ct        9    10


Column Summary
--------------

Number of columns in common: 9
Number of columns in tsm_smj_ct but not in cal_tsm_smj_ct: 0
Number of columns in cal_tsm_smj_ct but not in tsm_smj_ct: 0

Row Summary
-----------

Matched on: smj_code
Any duplicates on match values: No
Default Absolute Tolerance: 0.0001
Default Relative Tolerance: 0
Number of rows in common: 10
Number of rows in tsm_smj_ct but not in cal_tsm_smj_ct: 0
Number of rows in cal_tsm_smj_ct but not in tsm_smj_ct: 0

Number of rows with some compared columns unequal: 10
Number of rows with all compared columns equal: 0

Column Comparison
-----------------

Number of columns compared with some values unequal: 2
Number of columns compared with all values equal: 7
Total number of values which compare unequal: 11

Columns with Unequal Values or Types
------------------------------------

Column               tsm_smj_ct dtype cal_tsm_smj_ct dtype  # Unequal   Max Diff  # Null Diff    Rel Tol    Abs Tol
-------------------- --------------- --------------- ---------- ---------- ------------ ---------- ----------
last_mod_date        datetime64[ns]  datetime64[ns]           1     0.0000            0     0.0000     0.0001
timestamp            object          object                  10     0.0000            0     0.0000     0.0001


Sample Rows with Unequal Values
-------------------------------

  smj_code last_mod_date (tsm_smj_ct) last_mod_date (cal_tsm_smj_ct)
0     ITMP    2025-12-05 14:38:16.916        2025-12-04 11:34:20.523

    smj_code            timestamp (tsm_smj_ct)        timestamp (cal_tsm_smj_ct)
0       GTSM  b'\x00\x02\x00\x00r\xd1\xe9\xc4'  b'\x00\x02\x00\x00r\xec\x0b\x82'
1       CRIM     b'\x00\x02\x00\x00r\xbe\xc5Z'     b'\x00\x02\x00\x00r\xec\x0b|'
2       TSCI  b'\x00\x02\x00\x00r\xbe\x97\xe6'     b'\x00\x02\x00\x00r\xec\x0bz'
3       AISS  b'\x00\x02\x00\x00r\xbe\x97\xcf'  b'\x00\x02\x00\x00r\xec\x0b\x88'
4       DGET  b'\x00\x02\x00\x00r\xbe\x97\xd8'     b'\x00\x02\x00\x00r\xec\x0b~'
5       AIDS  b'\x00\x02\x00\x00r\xbe\x97\xcc'  b'\x00\x02\x00\x00r\xec\x0b\x8a'
6       CUIM  b'\x00\x02\x00\x00r\xbe\x97\xd5'  b'\x00\x02\x00\x00r\xec\x0b\x86'
7  TEST_DEPT  b'\x00\x02\x00\x00r\xbe\x97\xe4'  b'\x00\x02\x00\x00r\xec\x0b\x8c'
8       ITMP     b'\x00\x02\x00\x00sx\x0e\xfe'  b'\x00\x02\x00\x00r\xec\x0b\x84'
9       EIMT  b'\x00\x02\x00\x00r\xbe\x97\xdb'  b'\x00\x02\x00\x00r\xec\x0b\x80'

Database connection closed.
'''