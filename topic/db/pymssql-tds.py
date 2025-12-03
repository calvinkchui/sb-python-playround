# WIP
import pymssql

print(pymssql.version_info());

conn = pymssql.connect(
    server='', port=6003, user='', password='', database='', charset='utf8'
   ,tds_version='5.0' 
) 
   # use tds_version='5.0' if needed
'''
  File "C:\calvin\dev\sb-python-playround\topic\db\db-pymssql.py", line 5, in <module>
    conn = pymssql.connect(
           ^^^^^^^^^^^^^^^^
  File "src/pymssql/_pymssql.pyx", line 650, in pymssql._pymssql.connect
  File "src/pymssql/_mssql.pyx", line 2168, in pymssql._mssql.connect
  File "src/pymssql/_mssql.pyx", line 665, in pymssql._mssql.MSSQLConnection.__init__
  File "src/pymssql/_mssql.pyx", line 1989, in pymssql._mssql._tds_ver_str_to_constant
pymssql._mssql.MSSQLException: unrecognized tds version: 5.0
'''
   
# cur = conn.cursor()

#cur.execute("SELECT TOP 10 * FROM your_table")
#rows = cur.fetchall()

#print(rows)