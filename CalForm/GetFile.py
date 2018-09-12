# _*_coding:utf-8 _*_
import os


class GetFile(object):

    @staticmethod
    def get_file_name(path):
        files = os.listdir(path)
        # print files
        return files