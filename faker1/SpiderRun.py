# _*_coding:utf-8 _*_
from DataOutput import DataOutput
from HTMLDownloader import HTMLDownloader
from HTMLParse import HTMLParse
from URLManage import URLManage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class SpiderRun(object):
    '''
    爬虫调度主程序
    '''
    def __init__(self):
        self.manager = URLManage()
        self.parser = HTMLParse()
        self.downloader = HTMLDownloader()
        self.output = DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 5:
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "抓取URL:", new_url
                print "已经抓取{}个链接".format(self.manager.old_url_size())
            except Exception, e:
                print "Exception is:", e
        self.output.output_html()
        print self.manager.new_url_size()
        print self.output.datas_size()
if __name__ == "__main__":
    spider = SpiderRun()
    spider.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")


