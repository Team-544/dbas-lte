import pyodbc


class DatabaseManipulate:
    driver = 'ODBC Driver 17 for SQL Server'
    server = 'TWISTSURFACE\SQLEXPRESS'
    database = 'TD_LTE'
    admin_id = 'twist'
    admin_pwd = 'sql998541'

    col_names_dict = {'tbKPI': [], 'tbPRB': ['起始时间', '周期', '网元名称', '小区', '小区名']}

    def __init__(self):
        self.__admin_cnxn = pyodbc.connect(DRIVER=self.driver,
                                           SERVER=self.server,
                                           DATABASE=self.database,
                                           UID=self.admin_id,
                                           PWD=self.admin_pwd)

    def register(self, username, password):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute(
            "create login " + username + " with password='" + password + "', default_database=TD_LTE")
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

    def getTables(self):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute("SELECT NAME FROM SYSOBJECTS WHERE TYPE='U'")
        table_names = list()
        for tuple in admin_cursor.fetchall():
            table_names.append(tuple[0])
        return table_names

    def getCells(self):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute("SELECT DISTINCT SECTOR_ID, SECTOR_NAME FROM tbCell")
        cells = list()
        for tuple in admin_cursor.fetchall():
            cells.append(tuple[0])
            cells.append(tuple[1])
        return cells

    def getENodeBs(self):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute("SELECT DISTINCT ENODEBID, ENODEB_NAME FROM tbCell")
        eNodeBs = list()
        for tuple in admin_cursor.fetchall():
            eNodeBs.append(str(tuple[0]))
            eNodeBs.append(tuple[1])
        return eNodeBs

    def getNENames(self, tb_name):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute("SELECT DISTINCT [网元名称] FROM %s" % tb_name)
        NE_names = list()
        for tuple in admin_cursor.fetchall():
            NE_names.append(tuple[0])
        return NE_names

    def getTbCols(self, tb_name):
        admin_cursor = self.__admin_cnxn.cursor()
        admin_cursor.execute("select name from syscolumns where id=object_id('%s')" % tb_name)
        cols = list()
        for tuple in admin_cursor.fetchall():
            if tuple[0] not in ['起始时间', '周期', '网元名称', '小区', '小区名']:
                cols.append(tuple[0])
        return cols

    def doSQL(self, sql):
        user_cursor = self.user_cnxn.cursor()
        user_cursor.execute(sql)
        for line in user_cursor:
            print(line)


if __name__ == '__main__':
    dbm = DatabaseManipulate()
    for name in dbm.getENodeB():
        print(name)
