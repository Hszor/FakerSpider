# _*_coding:utf-8 _*_
import requests


class HTMLDownloader(object):
    @staticmethod
    def download(url):
        '''
        先设置为静态方法，因为此下载器与类的URL无关
        :param url:
        :return:
        '''
        if url is None:
            return
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109' \
                     ' Safari/537.36'
        headers = {'User-Agent':user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        return None
