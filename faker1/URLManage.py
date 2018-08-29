# _*_coding:utf-8 _*_
class URLManage(object):
    def __init__(self):
        self.new_urls = set()    #未爬取的URL
        self.old_urls = set()    #已爬取的URL

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0

    def get_new_url(self):
        '''
        获取一个未爬取的URL
        :return:
        '''
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        '''
        增加一个未爬取URL
        :return:
        '''
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        '''
        增加多个URL，参数为URL的列表
        :param urls:
        :return:
        '''
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        '''
        获取未爬取的URL大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已爬取的URL大小
        :return:
        '''
        return len(self.old_urls)