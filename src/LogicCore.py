import datetime
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

    def data_export(self, file_type, file_path, file_name):  # file_type——导出文件的类型；file_path——导出文件的路径；file_name——导出文件的名称
        path = file_path.replace("\\", "/")
        split_num = path.count("/")
        path_dir = ""
        for ch in path:
            if split_num > 0:
                if ch == '/':
                    split_num -= 1
                path_dir += ch
        file = Path(path_dir)
        if not file.is_dir():
            print("文件不存在 ！")
            # TODO: 错误处理
        if file_type == '.xls' or file_type == '.xlsx':
            if path[-4:] != ".xls" and path[-5:] != ".xlsx":
                print("格式不正确, 请检查后缀")
            cursor = connect.cnxn.cursor()
            if file_name == 'tbCell':
                cursor.execute('select * from teCell')
                table = cursor.fetchall()
                field_list = ['CITY', 'SECTOR_ID', 'SECTOR_NAME', 'ENODEBID', 'ENODEB_NAME', 'EARFCN', 'PCI',
                              'PSS', 'SSS', 'TAC', 'VENDOR', 'LONGITUDE', 'LATITUDE', 'STYLE', 'AZIMUTH',
                              'HEIGHT', 'ELECTTILT', 'MECHTILT', 'TOTLETILT']
            if file_name == 'tbKPI':
                cursor.execute('select * from tbKPI')
                table = cursor.fetchall()
                field_list = [u'起始时间', '周期', '网元名称', '小区', '小区名', 'RRC连接建立完成次数 (无)',
                              'RRC连接请求次数（包括重发） (无)', 'RRC建立成功率qf (%)', 'E-RAB建立成功总次数 (无)',
                              'E-RAB建立尝试总次数 (无)', 'E-RAB建立成功率2 (%)', 'eNodeB触发的E-RAB异常释放总次数 (无)',
                              '小区切换出E-RAB异常释放总次数 (无)', 'E-RAB掉线率(新) (%)', '无线接通率ay (%)',
                              'eNodeB发起的S1 RESET导致的UE Context释放次数 (无)', 'UE Context异常释放次数 (无)',
                              'UE Context建立成功总次数 (无)', '无线掉线率 (%)', 'eNodeB内异频切换出成功次数 (无)',
                              'eNodeB内异频切换出尝试次数 (无)', 'eNodeB内同频切换出成功次数 (无)', 'eNodeB内同频切换出尝试次数 (无)',
                              'eNodeB间异频切换出成功次数 (无)', 'eNodeB间异频切换出尝试次数 (无)', 'eNodeB间同频切换出成功次数 (无)',
                              'eNodeB间同频切换出尝试次数 (无)', 'eNB内切换成功率 (%)', 'eNB间切换成功率 (%)',
                              '同频切换成功率zsp (%)', '异频切换成功率zsp (%)', '切换成功率 (%)',
                              '小区PDCP层所接收到的上行数据的总吞吐量 (比特)', '小区PDCP层所发送的下行数据的总吞吐量 (比特)',
                              'RRC重建请求次数 (无)', 'RRC连接重建比率 (%)',
                              '通过重建回源小区的eNodeB间同频切换出执行成功次数 (无)', '通过重建回源小区的eNodeB间异频切换出执行成功次数 (无)',
                              '通过重建回源小区的eNodeB内同频切换出执行成功次数 (无)', '通过重建回源小区的eNodeB内异频切换出执行成功次数 (无)',
                              'eNB内切换出成功次数 (次)', 'eNB内切换出请求次数 (次)']
            if file_name == 'tbPRB':
                cursor.execute('select * from tbPRB')
                table = cursor.fetchall()
                field_list = [u'起始时间', '周期', '网元名称', '小区', '小区名',
                              'avg_prb0', 'avg_prb1', 'avg_prb2', 'avg_prb3', 'avg_prb4', 'avg_prb5', 'avg_prb6',
                              'avg_prb7', 'avg_prb8', 'avg_prb9',
                              'avg_prb10', 'avg_prb11', 'avg_prb12', 'avg_prb13', 'avg_prb14', 'avg_prb15', 'avg_prb16',
                              'avg_prb17', 'avg_prb18', 'avg_prb19',
                              'avg_prb20', 'avg_prb21', 'avg_prb22', 'avg_prb23', 'avg_prb24', 'avg_prb25', 'avg_prb26',
                              'avg_prb27', 'avg_prb28', 'avg_prb29',
                              'avg_prb30', 'avg_prb31', 'avg_prb32', 'avg_prb33', 'avg_prb34', 'avg_prb35', 'avg_prb36',
                              'avg_prb37', 'avg_prb38', 'avg_prb39',
                              'avg_prb40', 'avg_prb41', 'avg_prb42', 'avg_prb43', 'avg_prb44', 'avg_prb45', 'avg_prb46',
                              'avg_prb47', 'avg_prb48', 'avg_prb49',
                              'avg_prb50', 'avg_prb51', 'avg_prb52', 'avg_prb53', 'avg_prb54', 'avg_prb55', 'avg_prb56',
                              'avg_prb57', 'avg_prb58', 'avg_prb59',
                              'avg_prb60', 'avg_prb61', 'avg_prb62', 'avg_prb63', 'avg_prb64', 'avg_prb65', 'avg_prb66',
                              'avg_prb67', 'avg_prb68', 'avg_prb69',
                              'avg_prb70', 'avg_prb71', 'avg_prb72', 'avg_prb73', 'avg_prb74', 'avg_prb75', 'avg_prb76',
                              'avg_prb77', 'avg_prb78', 'avg_prb79',
                              'avg_prb80', 'avg_prb81', 'avg_prb82', 'avg_prb83', 'avg_prb84', 'avg_prb85', 'avg_prb86',
                              'avg_prb87', 'avg_prb88', 'avg_prb89',
                              'avg_prb90', 'avg_prb91', 'avg_prb92', 'avg_prb93', 'avg_prb94', 'avg_prb95', 'avg_prb96',
                              'avg_prb97', 'avg_prb98', 'avg_prb99']
            if file_name == 'tbMROData':
                cursor.execute('select * from tbMROData')
                table = cursor.fetchall()
                field_list = ['TimeStamp', 'ServingSector', 'InterferingSector',
                              'LteScRSRP', 'LteNcRSRP', 'LteNcEarfcn', 'LteNcPci']
            if file_name == 'tbAdjCell':
                cursor.execute('select * from tbAdjCell')
                table = cursor.fetchall()
                field_list = ['S_SECTOR_ID', 'N_SECTOR_ID', 'S_EARFCN', 'N_EARFCN']
            if file_name == 'tbATUC2I':
                cursor.execute('select * from tbATUC2I')
                table = cursor.fetchall()
                field_list = ['SECTOR_ID', 'NCELL_ID', 'RATIO_ALL', 'RANK', 'COSITE']
            if file_name == 'tbATUData':
                cursor.execute('select * from tbATUData')
                table = cursor.fetchall()
                field_list = ['seq', 'FileName', 'Time', 'Longitude', 'Latitude',
                              'CellID', 'TAC', 'EARFCN', 'PCI', 'RSRP', 'RS_SINR',
                              'NCell_ID_1', 'NCell_EARFCN_1', 'NCell_PCI_1', 'NCell_RSRP_1',
                              'NCell_ID_2', 'NCell_EARFCN_2', 'NCell_PCI_2', 'NCell_RSRP_2',
                              'NCell_ID_3', 'NCell_EARFCN_3', 'NCell_PCI_3', 'NCell_RSRP_3',
                              'NCell_ID_4', 'NCell_EARFCN_4', 'NCell_PCI_4', 'NCell_RSRP_4',
                              'NCell_ID_5', 'NCell_EARFCN_5', 'NCell_PCI_5', 'NCell_RSRP_5',
                              'NCell_ID_6', 'NCell_EARFCN_6', 'NCell_PCI_6', 'NCell_RSRP_6']
            if file_name == 'tbATUHandOver':
                cursor.execute('select * from tbATUHandOver')
                table = cursor.fetchall()
                field_list = ['SSECTOR_ID', 'NSECTOR_ID', 'HOATT']
            if file_name == 'tbC2I':
                cursor.execute('select * from tbC2I')
                table = cursor.fetchall()
                field_list = ['CITY', 'SCELL', 'NCELL', 'PrbC2I9', 'C2I_Mean', 'std', 'SampleCount', 'WeightedC2I']
            if file_name == 'tbC2I3':
                cursor.execute('select * from tbC2I3')
                table = cursor.fetchall()
                field_list = ['CELL1', 'CELL2', 'CELL3']
            if file_name == 'tbC2Inew':
                cursor.execute('select * from tbC2Inew')
                table = cursor.fetchall()
                field_list = ['SCELL', 'NCELL', 'C2I_Mean', 'Std', 'PrbC2I9', 'PrbABS6']
            if file_name == 'tbHandOver':
                cursor.execute('select * from tbHandOver')
                table = cursor.fetchall()
                field_list = ['CITY', 'SCELL', 'NCELL', 'HOATT', 'HOSUCC', 'HOSUCCRATE']
            if file_name == 'tbOptCell':
                cursor.execute('select * from tbOptCell')
                table = cursor.fetchall()
                field_list = ['SECTOR_ID', 'EARFCN', 'CELL_TYPE']
            if file_name == 'tbPCIAssignment':
                cursor.execute('select * from tbPCIAssignment')
                table = cursor.fetchall()
                field_list = ['ASSIGN_ID', 'EARFCN', 'SECTOR_ID', 'SECTOR_NAME', 'ENODEB_ID', 'PCI',
                              'PSS', 'SSS', 'LONGITUDE', 'LATITUDE', 'STYLE', 'OPT_DATETIME']
            if file_name == 'tbSecAdjcell':
                cursor.execute('select * from tbSecAdjcell')
                table = cursor.fetchall()
                field_list = ['S_SECTOR_ID', 'N_SECTOR_ID']
            workbook = xlwt.Workbook(encoding='gbk')
            # 创建Excel中的一个sheet，并命名且为可重写状态
            sheet = workbook.add_sheet('sheet0', cell_overwrite_ok=True)
            # 将上述list中各字段的列名称依次填入Excel中去
            for field in range(0, len(field_list)):
                sheet.write(0, field, field_list[field])
            # 根据横纵坐标依次录入查询到的信息值
            row = 1
            col = 0
            for row in range(1, len(table) + 1):
                for col in range(0, len(field_list)):
                    sheet.write(row, col, u'%s' % table[row - 1][col])
            sheet_time = datetime.datetime.now()
            book_mark = sheet_time.strftime('%Y%m%d')
            workbook.save(path)
            print("导出成功！")

        elif file_type == '.txt':
            if path[-4:0] != ".txt":
                print("文件格式不正确！")
            f = open(path, "w+")
            cursor = connect.cnxn.cursor()
            if file_name == 'tbCell':
                cursor.execute('select * from tbCell')
                table = cursor.fetchall()
                f.write("CITY, SECTOR_ID, SECTOR_NAME, ENODEB_ID, ENODEB_NAME, EARFCN, PCI, PSS, SSS, TAC, "
                        "VENDOR, LONGITUDE, LATITUDE, STYLE, AZIMUTH, HEIGHT, ELECTTILT, MECHTILT, TOTLETILT")
            if file_name == 'tbKPI':
                cursor.execute('select * from tbKPI')
                table = cursor.fetchall()
                f.write("起始时间, 周期, 网元名称, 小区, 小区名, RRC连接建立完成次数 (无), "
                        "RRC连接请求次数（包括重发） (无), RRC建立成功率 (%), E-RAB建立成功总次数 (无), "
                        "E-RAB建立尝试总次数 (无), E-RAB建立成功率2 (%), eNodeB触发的E-RAB异常释放总次数 (无), "
                        "小区切换出E-RAB异常释放总次数 (无), E-RAB掉线率(新) (%), 无线接通率ay (%), "
                        "eNodeB发起的S1 RESET导致的UE Context释放次数 (无), UE Context异常释放次数 (无), "
                        "UE Context建立成功总次数 (无), 无线掉线率 (%), eNodeB内异频切换出成功次数 (无), "
                        "eNodeB内异频切换出尝试次数 (无), eNodeB内同频切换出成功次数 (无), eNodeB内同频切换出尝试次数 (无), "
                        "eNodeB间异频切换出成功次数 (无), eNodeB间异频切换出尝试次数 (无), eNodeB间同频切换出成功次数 (无), "
                        "eNodeB间同频切换出尝试次数 (无), eNB内切换成功率 (%), eNB间切换成功率 (%), "
                        "同频切换成功率zsp (%), 异频切换成功率zsp (%), '切换成功率 (%), "
                        "小区PDCP层所接收到的上行数据的总吞吐量 (比特), 小区PDCP层所发送的下行数据的总吞吐量 (比特), "
                        "RRC重建请求次数 (无), RRC连接重建比率 (%), "
                        "通过重建回源小区的eNodeB间同频切换出执行成功次数 (无), 通过重建回源小区的eNodeB间异频切换出执行成功次数 (无), "
                        "通过重建回源小区的eNodeB内同频切换出执行成功次数 (无), 通过重建回源小区的eNodeB内异频切换出执行成功次数 (无), "
                        "eNB内切换出成功次数 (次), eNB内切换出请求次数 (次)")
            if file_name == 'tbPRB':
                cursor.execute('select * from tbPRB')
                table = cursor.fetchall()
                f.write("起始时间, 周期, 网元名称, 小区, 小区名, "
                        "avg_prb0, avg_prb1, avg_prb2, avg_prb3, avg_prb4, avg_prb5, avg_prb6, avg_prb7, avg_prb8, "
                        "avg_prb9, "
                        "avg_prb10, avg_prb11, avg_prb12, avg_prb13, avg_prb14, avg_prb15, avg_prb16, avg_prb17, "
                        "avg_prb18, avg_prb19, "
                        "avg_prb20, avg_prb21, avg_prb22, avg_prb23, avg_prb24, avg_prb25, avg_prb26, avg_prb27, "
                        "avg_prb28, avg_prb29, "
                        "avg_prb30, avg_prb31, avg_prb32, avg_prb33, avg_prb34, avg_prb35, avg_prb36, avg_prb37, "
                        "avg_prb38, avg_prb39, "
                        "avg_prb40, avg_prb41, avg_prb42, avg_prb43, avg_prb44, avg_prb45, avg_prb46, avg_prb47, "
                        "avg_prb48, avg_prb49, "
                        "avg_prb50, avg_prb51, avg_prb52, avg_prb53, avg_prb54, avg_prb55, avg_prb56, avg_prb57, "
                        "avg_prb58, avg_prb59, "
                        "avg_prb60, avg_prb61, avg_prb62, avg_prb63, avg_prb64, avg_prb65, avg_prb66, avg_prb67, "
                        "avg_prb68, avg_prb69, "
                        "avg_prb70, avg_prb71, avg_prb72, avg_prb73, avg_prb74, avg_prb75, avg_prb76, avg_prb77, "
                        "avg_prb78, avg_prb79, "
                        "avg_prb80, avg_prb81, avg_prb82, avg_prb83, avg_prb84, avg_prb85, avg_prb86, avg_prb87, "
                        "avg_prb88, avg_prb89, "
                        "avg_prb90, avg_prb91, avg_prb92, avg_prb93, avg_prb94, avg_prb95, avg_prb96, avg_prb97, "
                        "avg_prb98, avg_prb99")
            if file_name == 'tbMROData':
                cursor.execute('select * from tbMROData')
                table = cursor.fetchall()
                f.write("TimeStamp, ServingSector, InterferingSector, LteScRSRP, LteNcRSRP, LteNcEarfcn, LteNcPci")
            if file_name == 'tbAdjCell':
                cursor.execute('select * from tbAdjCell')
                table = cursor.fetchall()
                f.write("S_SECTOR_ID, N_SECTOR_ID, S_EARFCN, N_EARFCN")
            if file_name == 'tbATUC2I':
                cursor.execute('select * from tbATUC2I')
                table = cursor.fetchall()
                f.write("SECTOR_ID, NCELL_ID, RATIO_ALL, RANK, COSITE")
            if file_name == 'tbATUData':
                cursor.execute('select * from tbATUData')
                table = cursor.fetchall()
                f.write("seq, FileName, Time, Longitude, Latitude, "
                        "CellID, TAC, EARFCN, PCI, RSRP, RS_SINR, "
                        "NCell_ID_1, NCell_EARFCN_1, NCell_PCI_1, NCell_RSRP_1, "
                        "NCell_ID_2, NCell_EARFCN_2, NCell_PCI_2, NCell_RSRP_2, "
                        "NCell_ID_3, NCell_EARFCN_3, NCell_PCI_3, NCell_RSRP_3, "
                        "NCell_ID_4, NCell_EARFCN_4, NCell_PCI_4, NCell_RSRP_4, "
                        "NCell_ID_5, NCell_EARFCN_5, NCell_PCI_5, NCell_RSRP_5, "
                        "NCell_ID_6, NCell_EARFCN_6, NCell_PCI_6, NCell_RSRP_6")
            if file_name == 'tbATUHandOver':
                cursor.execute('select * from tbATUHandOver')
                table = cursor.fetchall()
                f.write("S_SECTOR_ID, N_SECTOR_ID, HOATT")
            if file_name == 'tbC2I':
                cursor.execute('select * from tbC2I')
                table = cursor.fetchall()
                f.write("CITY, SCELL, NCELL, PrbC2I9, C2I_Mean, Std, SampleCount, WeightedC2I")
            if file_name == 'tbC2I3':
                cursor.execute('select * from tbC2I3')
                table = cursor.fetchall()
                f.write("CELL1, CELL2, CELL3")
            if file_name == 'tbC2Inew':
                cursor.execute('select * from tbC2Inew')
                table = cursor.fetchall()
                f.write("SCELL, NCELL, C2I_Mean, Std, PrbC2I9, PrbABS6")
            if file_name == 'tbHandOver':
                cursor.execute('select * from tbHandOver')
                table = cursor.fetchall()
                f.write("CITY, SCELL, NCELL, HOATT, HOUSUCC, HOUSUCCRATE")
            if file_name == 'tbOptCell':
                cursor.execute('select * from tbOptCell')
                table = cursor.fetchall()
                f.write("SECTOR_ID, EARFCN, CELL_TYPE")
            if file_name == 'tbPCIAssignment':
                cursor.execute('select * from tbPCIAssigment')
                table = cursor.fetchall()
                f.write("ASSIGN_ID, EARFCN, SECTOR_ID, SECTOR_NAME, ENODEB_ID, PCI, "
                        "PSS, SSS, LONGITUDE, LATITUDE, STYLE, OPT_DATETIME")
            if file_name == 'tbSecAdjcell':
                cursor.execute('select * from tbSecAdjcell')
                table = cursor.fetchall()
                f.write("S_SECTOR_ID, N_SECTOR_ID")
            f.write('\n')
            for row in range(len(table)):
                f.write(str(table[row]))
                f.write('\n')
            f.close()
            connect.cnxn.commit()
            print("导出成功！")

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
        if str(value).count('.') == 1:
            num_left = int(value)
            num_right = value - int(value)
            if num_left != '0' or not (num_right.isdigit()):
                print('输入的数字应为0~1之间的小数！')
                # TODO：错误处理
        else:
            print('输入的数字应为0~1之间的小数！')
            # TODO：错误处理
        cursor = connect.cnxn.cursor()
        cursor.execute('delete from tbC2I3')
        connect.cnxn.commit()
        cursor = connect.cnxn.cursor()
        cursor.execute('delete from tbC2Inew')
        connect.cnxn.commit()
        cursor = connect.cnxn.cursor()
        cursor.execute('exec storeInC2I ?', messure_std)
        connect.cnxn.commit()
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
        return result


if __name__ == '__main__':
    lc = LogicCore()
    # lc.data_import('.xlsx', 'C:/Workspace/学习/数据库课程设计/数据库系统原理课程设计/4-1. 三门峡地区TD-LTE网络数据/1.tbCell.xlsx', 'tbCell')
    # lc.data_export('.txt', 'C:/TD-LTE/tbcell.txt', 'tbCell')
