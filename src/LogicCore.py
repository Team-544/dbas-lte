from time import sleep

import pyodbc

from src.DB import DatabaseManipulate

import connect  # 用于数据库的连接
import csv  # 用于csv文件的读写
import xlrd  # 读Excel文件的库
import xlwt  # 写Excel文件的库
import re  # 检验字符串中是否包含中文
import pyodbc
import pymssql

# 临时表，用于bulk insert
test_addr = "C:/TD-LTE/temp.csv"
# RSRP测量值对的数量筛选标准，测量值对数量小于此标准则被筛掉
messure_std = 5
partition = 20  # 将数据以50行为一组写入


class LogicCore:
    # def __init__(self, ui):
    #     self.ui = ui
    #     try:
    #         self.db = DatabaseManipulate()
    #     except (pyodbc.InterfaceError, pyodbc.OperationalError):
    #         self.ui.showStatus("Failed to connect to database system.")

    def signIn(self, username, password):
        try:
            self.db.signIn(username, password)
            return True
        except pyodbc.InterfaceError :
            self.ui.showStatus("Wrong user name or password.")
            return False

    def logOut(self):
        self.db.user_cnxn.close()
        self.db.user_cnxn = None

    def register(self, username, password):
        try:
            self.db.register(username, password)
            self.ui.showStatus("Your account is available now, please sign in.")
        except pyodbc.ProgrammingError:
            self.ui.showStatus("Your username is illegal, please try another one.")

    def data_import(self, file_type, file_path, file_name):  # file_type——导入文件的类型；file_path——导入文件的路径；file_name——导入表格的名称;
        if file_type == '.xlsx' or file_type == '.xls':
            try:
                data = xlrd.open_workbook(file_path)  # 打开目标文件
            except:
                print('File %s open error!\n' % (file_name))  # TODO：异常处理
            table = data.sheets()[0]  # 获取表格
            num = table.nrows  # 统计表格的行数
            if file_name == 'tbCell':
                row = 1
                while row < num:
                    InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                    csv_writer = csv.writer(InputBuffer)
                    i = 0
                    while i < partition and row < num:
                        item = table.row_values(row)
                        item[3] = int(item[3])
                        item[5] = int(item[5])
                        item[6] = int(item[6])
                        item[8] = int(item[8])
                        item[7] = int(item[7])
                        item[9] = int(item[9])
                        if (item[15] is not ''):
                            item[15] = int(item[15])

                        csv_writer.writerow(item)
                        i += 1
                        row += 1
                    InputBuffer.close()
                    cursor = connect.cnxn.cursor()
                    print(test_addr)
                    cursor.execute(
                        "bulk insert tbCell from '%s' with (FIELDTERMINATOR = ',', FIRE_TRIGGERS);" % test_addr)
                    connect.cnxn.commit()
            elif file_name == 'tbKPI':  # 此处应当激活触发器
                row = 1
                while row < num:
                    InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                    csv_writer = csv.writer(InputBuffer)
                    i = 0

                    while i < partition and row < num:
                        item = table.row_values(row)
                        err = [1, 5, 6, 8, 9, 11, 12, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 32, 33, 34] + [i for i in range(36, 42)]
                        for num in err:
                            item[num] = int(item[num])

                        csv_writer.writerow(item)
                        i += 1
                        row += 1
                    InputBuffer.close()
                    cursor = connect.cnxn.cursor()
                    cursor.execute("bulk insert tbKPI from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
                    connect.cnxn.commit()
            elif file_name == 'tbPRB':
                row = 1
                while row < num:
                    InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                    csv_writer = csv.writer(InputBuffer)
                    i = 0
                    while i < partition and row < num:
                        item = table.row_values(row)
                        csv_writer.writerow(item)
                        i += 1
                        row += 1
                    InputBuffer.close()
                    cursor = connect.cnxn.cursor()
                    cursor.execute("bulk insert tbPRB from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
                    connect.cnxn.commit()
            elif file_name == 'tbPMROData':
                row = 1
                while row < num:
                    InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                    csv_writer = csv.writer(InputBuffer)
                    i = 0
                    while i < partition and row < num:
                        item = table.row_values(row)
                        csv_writer.writerow(item)
                        i += 1
                        row += 1
                    InputBuffer.close()
                    cursor = connect.cnxn.cursor()
                    cursor.execute("bulk insert tbPMROData from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
                    connect.cnxn.commit()
        elif type == '.csv':
            with open(file_path, 'w') as data:
                table = csv.reader(data)
                num = len(table)
                if file_name == 'tbCell':
                    row = 0
                    i = 0
                    for line in table:
                        row += 1
                        trueline = line.split(',')
                        if i == 0:
                            InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                            csv_writer = csv.writer(InputBuffer)
                        if row != 1:
                            csv_writer.writerow(trueline)
                            i += 1
                        if i == partition or row == num:
                            InputBuffer.close()
                            cursor = connect.cnxn.cursor()
                            cursor.execute("bulk insert tbCell from %s with (FIELDTERMINATOR = ',', FIRE_TRIGGERS);",
                                           test_addr)
                            connect.cnxn.commit()
                            i = 0
                elif file_name == 'tbKPI':
                    row = 0
                    i = 0
                    for line in table:
                        row += 1
                        trueline = line.split(',')
                        if i == 0:
                            InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                            csv_writer = csv.writer(InputBuffer)
                        if row != 1:
                            csv_writer.writerow(trueline)
                            i += 1
                        if i == partition or row == num:
                            InputBuffer.close()
                            cursor = connect.cnxn.cursor()
                            cursor.execute("bulk insert tbCell from %s with (FIELDTERMINATOR = ',', FIRE_TRIGGERS);",
                                           test_addr)
                            connect.cnxn.commit()
                            i = 0
                elif file_name == 'tbPRB':
                    row = 0
                    i = 0
                    for line in table:
                        row += 1
                        trueline = line.split(',')
                        if i == 0:
                            InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                            csv_writer = csv.writer(InputBuffer)
                        if row != 1:
                            csv_writer.writerow(trueline)
                            i += 1
                        if i == partition or row == num:
                            InputBuffer.close()
                            cursor = connect.cnxn.cursor()
                            cursor.execute("bulk insert tbCell from %s with (FIELDTERMINATOR = ',', FIRE_TRIGGERS);",
                                           test_addr)
                            connect.cnxn.commit()
                            i = 0
                elif file_name == 'tbMROData':
                    row = 0
                    i = 0
                    for line in table:
                        row += 1
                        trueline = line.split(',')
                        if i == 0:
                            InputBuffer = open(test_addr, 'w', encoding='gbk', newline='')
                            csv_writer = csv.writer(InputBuffer)
                        if row != 1:
                            csv_writer.writerow(trueline)
                            i += 1
                        if i == partition or row == num:
                            InputBuffer.close()
                            cursor = connect.cnxn.cursor()
                            cursor.execute("bulk insert tbCell from %s with (FIELDTERMINATOR = ',', FIRE_TRIGGERS);",
                                           test_addr)
                            connect.cnxn.commit()
                            i = 0


if __name__ == '__main__':
    lc = LogicCore()
    lc.data_import('.xlsx', 'C:/Workspace/学习/数据库课程设计/数据库系统原理课程设计/表12优化区17日-19日KPI指标统计表-0717至0719——tbKPI.xlsx', 'tbKPI')
