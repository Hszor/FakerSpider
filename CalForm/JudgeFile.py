# _*_coding:utf-8 _*_


class JudgeFile(object):

    @staticmethod
    def xls_file(filename):
        if filename[-4:] == ".xls":
            return True
        return False


# j = JudgeFile()
# print j.xls_file("a.xls")
