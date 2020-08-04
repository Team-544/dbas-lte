import pyodbc


class DatabaseManipulate:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'TWISTSURFACE\SQLEXPRESS'
    database = 'TD_LTE_NET_CONF'
    admin_id = 'twist'
    admin_pwd = 'sql998541'

    def __init__(self):
        self.__admin_cnxn = pyodbc.connect(DRIVER=self.driver,
                                           SERVER=self.server,
                                           DATABASE=self.database,
                                           UID=self.admin_id,
                                           PWD=self.admin_pwd)

    def register(self, username, password):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute(
            "create login " + username + " with password='" + password + "', default_database=TD_LTE_NET_CONF")
        admin_cursor.execute('create user ' + username + ' for login ' + username + ' with default_schema=dbo')
        admin_cursor.execute("exec sp_addrolemember 'db_datareader', '" + username + "'")
        admin_cursor.execute("exec sp_addrolemember 'db_datawriter', '" + username + "'")
        admin_cursor.commit()

    def signIn(self, username, password):
        self.user_cnxn = pyodbc.connect(DRIVER=self.driver,
                                        SERVER=self.server,
                                        DATABASE=self.database,
                                        UID=username,
                                        PWD=password)

    def doSQL(self, sql):
        user_cursor = self.user_cnxn.cursor()
        user_cursor.execute(sql)
        for line in user_cursor:
            print(line)


if __name__ == '__main__':
    dbm = DatabaseManipulate()
    dbm.signIn('123', '456')
