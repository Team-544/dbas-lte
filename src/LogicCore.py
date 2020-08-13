import datetime
import time
from time import sleep

import pyodbc
import pandas as pd
from src.DB import DatabaseManipulate

import connect  # 用于数据库的连接
import csv  # 用于csv文件的读写
import xlrd  # 读Excel文件的库
import xlwt  # 写Excel文件的库
import re  # 检验字符串中是否包含中文
import pyodbc
import pymssql
from pathlib import Path

# 临时表，用于bulk insert
test_addr = "C:/TD-LTE/temp.csv"
# RSRP测量值对的数量筛选标准，测量值对数量小于此标准则被筛掉
partition = 20  # 将数据以50行为一组写入


class LogicCore:
    def __init__(self, ui):
        self.ui = ui
        try:
            self.db = DatabaseManipulate()
        except (pyodbc.InterfaceError, pyodbc.OperationalError):
            self.ui.showStatus("Failed to connect to database system.")

    def signIn(self, username, password):
        try:
            self.db.signIn(username, password)
            return True
        except pyodbc.InterfaceError:
            self.ui.showStatus("Wrong user name or password.")
            return False

    def logOut(self):
        self.db.user_cnxn.close()
        self.db.user_cnxn = None

    def register(self, username, password):
        try:
            self.db.register(username, password)
            self.ui.showStatus("Your account is available now, please sign in.")
        except pyodbc.ProgrammingError as e:
            print(e.args)
            self.ui.showStatus("Your username is illegal, please try another one.")

    def myImport(self, progress, file_path, tb_name):
        for i in range(101):
            progress.setValue(i)
            time.sleep(0.03)
        return True

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
                        err = [1, 5, 6, 8, 9, 11, 12, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 32, 33, 34] + [i for i
                                                                                                                 in
                                                                                                                 range(
                                                                                                                     36,
                                                                                                                     42)]
                        for num in err:
                            item[num] = int(item[num])

                        csv_writer.writerow(item)
                        i += 1
                        row += 1
                    InputBuffer.close()
                    cursor = connect.cnxn.cursor()
                    cursor.execute(
                        "bulk insert tbKPI from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
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
                    cursor.execute(
                        "bulk insert tbPRB from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
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
                    cursor.execute(
                        "bulk insert tbPMROData from '%s' with (FIELDTERMINATOR =',', FIRE_TRIGGERS);" % test_addr)
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

    def data_export(self, file_path, tb_name):
        lines = self.db.getAll(tb_name)
        cols = list()
        for dsc in lines[0].cursor_description:
            cols.append(dsc[0])
        type = file_path.split('.')[-1]
        df = pd.DataFrame(columns=cols)
        for line in lines:
            df.loc[len(df)] = line
        if type in ['xls', 'xlsx']:
            df.to_excel(file_path, encoding='utf_8_sig', index=False)
        elif type == 'csv':
            df.to_csv(file_path, encoding='utf_8_sig', index=False)
        return True

    def data_wash_tbMROData(self, file_path, save_path):
        f = open(file_path)
        MROData = pd.read_csv(f)
        MROData.drop_duplicates(subset=['TimeStamp', 'ServingSector', 'InterferingSector'], keep='first', inplace=True)
        MROData.to_csv(save_path, index=None)

    # 小区配置信息查询
    def search_tbCell(self, info):  # info——查询的依据,可能为中文（小区名称CellName）或者英文（Cell_ID）
        cursor = connect.cnxn.cursor()
        zhmodel = re.compile(u'[\u4e00-\u9fa5]')
        re.match = zhmodel.search(str(info))
        if re.match:  # 查询的内容中含有中文，用SECTOR_NAME查询
            cursor.execute('select * from tbCell where SECTOR_NAME = ?', info)
        else:  # 查询的内容中不含中文，用SECTOR_ID查询
            cursor.execute('select * from tbCell where SECTOR_ID = ?', info)
        result = cursor.fetchall()
        """
        cursor.execute('select name from syscolumns where id=object_id('tbCell')')
        col = cursor.fetchall()
        reuslt = col + result
        """
        return result

    # 基站eNodeB信息查询
    def search_eNodeB(self, info):  # info——查询的依据,可能为中文（小区名称eNodeBName）或者英文（eNodeBID）
        cursor = connect.cnxn.cursor()
        zhmodel = re.compile(u'[\u4e00-\u9fa5]')
        re.match = zhmodel.search(str(info))
        if re.match:  # 查询的内容中含有中文，用ENODEB_NAME查询
            cursor.execute('select * from tbCell where ENODEB_NAME = ?', info)
        else:  # 查询的内容中不含中文，用ENODEB_ID查询
            cursor.execute('select * from tbCell where ENODEBID = ?', info)
        result = cursor.fetchall()
        return result

    # KPI指标查询
    def search_KPI(self, info, start, end, attr):  # info——网元名称, start——起始时间， end——终止时间
        start = start + (' 00:00:00')
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        start = start.strftime('%m/%d/%Y %H:%M:%S')
        end = end + (' 00:00:00')
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        end = end.strftime('%m/%d/%Y %H:%M:%S')
        cursor = connect.cnxn.cursor()
        cursor.execute('select ? from tbKPI where 网元名称 = ? and 起始时间 between ? and ?', (attr, info, start, end))
        result = cursor.fetchall()
        length = len(result)
        date = [''] * int(length)
        attribute = [''] * int(length)
        cursor.execute('')  # TODO:查列表名称
        columns = cursor.fetchall()
        col = columns.index(attr)
        for i in range(length):
            date[i] = str(result[i][0])
            attribute[i] = result[i][col]
        return date, attribute

    # PRB信息查询
    def search_PRB(self, info, start, end, attr):  # info——网元名称；start——起始时间；end——结束时间；attr——网元的属性
        start = start.replace('T', ' ')
        start = start + ':00'
        start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        start = start.strftime('%m/%d/%Y %H:%M:%S')
        end = end.replace('T', ' ')
        end = end + ':00'
        end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        end = end.strftime('%m/%d/%Y %H:%M:%S')
        cursor = connect.cnxn.cursor(as_dict=True)
        cursor.execute('select ? from tbPRBnew where 小区名 = ? and 起始时间 between ? and ? ', (attr, info, start, end))
        result = cursor.fetchall()
        length = len(result)
        date = [''] * int(length)
        attribute = [''] * int(length)
        cursor.execute('Select Name FROM SysColumns Where id=Object_Id(tbKPI)')  # TODO:查列表名称
        columns = cursor.fetchall()
        col = columns.index(attr)
        for i in range(length):
            date[i] = str(result[i][0])
            attribute[i] = result[i][col]
        return date, attribute

    # 主邻小区C2I干扰分析
    def create_C2I_table(self, messure_std):
        cursor = connect.cnxn.cursor()
        cursor.execute('delete from tbC2Inew')
        connect.cnxn.commit()
        cursor = connect.cnxn.cursor()
        cursor.execute('exec storeInC2I ?', messure_std)  # 这里注意要传入用于筛选的参数
        connect.cnxn.commit()

    def C2I_interrupt_analysis(self, SCELL, NCELL):  # SCELL——主小区ID；NCELL——邻小区ID
        data = {'C2I_Mean': '', 'std': '', 'PrbC2I9': '', 'PrbABS6': ''}
        cursor = connect.cnxn.cursor()
        cursor.execute('select * from tbC2Inew where SCELL=? and NCELL=?', (SCELL, NCELL))
        result = cursor.fetchall()
        if len(result) != 0:
            mean = result[0][2]
            std = result[0][3]
            PRB9 = st.norm.cdf(9, loc=mean, scale=std)
            PRB6 = st.norm.cdf(6, loc=mean, scale=std) - st.norm.cdf(-6, loc=mean, scale=std)
            data['C2I_Mean'] = mean
            data['std'] = std
            data['PrbC2I9'] = PRB9
            data['PrbABS6'] = PRB6
        return data

    # 查询重叠覆盖干扰三元组
    def trigroup_search(self, value):  # value——查询的基准
        print('ready to search')
        cursor = connect.cnxn.cursor()
        cursor.execute('select SCELL, NCELL, C2I_Mean, std from tbC2Inew')
        result = cursor.fetchall()
        print(result)
        for i in range(len(result)):
            SCELL = result[i][0]  # SCELL
            NCELL = result[i][1]  # NCELL
            if result[i][3] != 0:  # std
                PRB9 = st.norm.cdf(9, loc=result[i][2], scale=result[i][3])
                PRB6 = st.norm.cdf(6, loc=result[i][2], scale=result[i][3])
            else:
                PRB9 = 0
                PRB6 = 0
            cursor.execute('update tbC2Inew set PrbC2I9=?, PrbABS6=? where SCELL=? and NCELL=?',
                           (PRB9, PRB6, SCELL, NCELL))
            connect.cnxn.commit()
        cursor = connect.cnxn.cursor()
        cursor.execute('exec insertTBC2I3 ?', value)
        connect.cnxn.commit()
        cursor = connect.cnxn.cursor()
        cursor.execute('select * from tbC2I3')
        result = cursor.fetchall()
        print(result)
        return result


if __name__ == '__main__':
    lc = LogicCore()
    # lc.data_import('.xlsx', 'C:/Workspace/学习/数据库课程设计/数据库系统原理课程设计/4-1. 三门峡地区TD-LTE网络数据/1.tbCell.xlsx', 'tbCell')
    # lc.data_export('.txt', 'C:/TD-LTE/tbcell.txt', 'tbCell')
