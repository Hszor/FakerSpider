# _*_coding:utf-8 _*_
from GetFile import GetFile
from JudgeFile import JudgeFile
from xlrd import open_workbook
from xlwt import Workbook
path = r"C:\test"

class CalForm(object):

    def __init__(self):
        self.file = GetFile()
        self.judge = JudgeFile()

    def cal(self, path):
        filenames = self.file.get_file_name(path)
        print filenames
        if filenames is not None:
            for filename in filenames:
                filename = path + '\\' + filename.decode('gb2312')
                print filename
                wb = open_workbook(filename)
                sheet_0 = wb.sheets()[0]
                total_rows = sheet_0.nrows
                total_cols = sheet_0.ncols

                array = [[0 for j in range(total_cols)]for i in range(total_rows)]
                # print array
                for row in range(total_rows):
                    for col in range(total_cols):
                        if isinstance(sheet_0.cell(row, col).value, (int, long, float)):
                            print sheet_0.cell(row, col).value
                            array[row][col] += sheet_0.cell(row, col).value

        print array

    def write_form(self, filename):


if __name__ == '__main__':
    cal_form = CalForm()
    cal_form.cal(path)
