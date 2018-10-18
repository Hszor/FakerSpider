# _*_coding:utf-8 _*_
from GetFile import GetFile
from JudgeFile import JudgeFile
from xlrd import open_workbook
from xlwt import Workbook
from xlutils.copy import copy

path = r"C:\test"
write_name = r"C:\test\7.xls"


class CalForm(object):
    def __init__(self):
        self.file = GetFile()
        self.judge = JudgeFile()
        self.form_num = 0 #表格总数
        # self.write_name = ""
        self.wb = ""
        self.datas = [] #存储总数数组
        # self.sheets = [] #存储表信息
        self.rows = [] #每个表的行数
        self.cols = [] #每个表的列数

    def cal(self, path):
        filenames = self.file.get_file_name(path)
        print filenames
        if filenames is not None:
            for filename in filenames:
                if self.judge.xls_file(filename):
                    filename = path + '\\' + filename.decode('gb2312')
                    print filename
                    rb = open_workbook(filename)

                    if self.wb == "":
                        self.wb = copy(rb)

                    if self.form_num == 0:
                        self.form_num = rb.nsheets
                    # if self.write_name == "":
                    #     self.write_name = filename
                    #     # self.copy_form(self.write_name)
                    #     self.wb = copy(rb)
                        # self.wb.save('C:\\test\\1.xls')

                    #初始化各项数据
                    if self.rows == []:
                        for i in range(self.form_num):
                            sheet_0 = rb.sheets()[i]
                            # self.sheets.append(rb.sheets()[i])
                            total_rows = sheet_0.nrows
                            self.rows.append(total_rows)
                            total_cols = sheet_0.ncols
                            self.cols.append(total_cols)
                            array = [[0 for j in range(total_cols)] for i in range(total_rows)]
                            self.datas.append(array)


                    #计算每个表格的和，存到datas
                    for i in range(self.form_num):
                        sheet_0 = rb.sheets()[i]
                        total_rows = sheet_0.nrows
                        total_cols = sheet_0.ncols
                        # print array
                        for row in range(total_rows):
                            for col in range(total_cols):
                                if isinstance(sheet_0.cell(row, col).value, (int, long, float)):
                                    print sheet_0.cell(row, col).value
                                    self.datas[i][row][col] += sheet_0.cell(row, col).value
                    # rb.close()

                print len(self.datas)
                self.write_form(self.wb, self.rows, self.cols)

    # def copy_form(self, filename):


    def write_form(self, wb, rows, cols):
        for i in range(self.form_num):
            ws = wb.get_sheet(i)
            for j in range(rows[i]):
                for k in range(cols[i]):
                    if isinstance(self.datas[i][j][k], (int, long, float)):
                        if self.datas[i][j][k] != 0:
                            ws.write(j, k, self.datas[i][j][k])
        wb.save(write_name)


if __name__ == '__main__':
    cal_form = CalForm()
    cal_form.cal(path)
