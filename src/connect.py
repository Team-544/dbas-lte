import pyodbc

driver = 'ODBC Driver 17 for SQL Server'
server = 'TWISTSURFACE\SQLEXPRESS'
database = 'TD_LTE'
admin_id = 'twist'
admin_pwd = 'sql998541'
cnxn = pyodbc.connect(DRIVER=driver,
                       SERVER=server,
                       DATABASE=database,
                       UID=admin_id,
                       PWD=admin_pwd)
