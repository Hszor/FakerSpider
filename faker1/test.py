# _*_coding:utf-8 _*_
from DataOutput import DataOutput
from HTMLDownloader import HTMLDownloader
from HTMLParse import HTMLParse
from URLManage import URLManage
from bs4 import BeautifulSoup
import re
s = HTMLDownloader()

t = s.download('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')

soup = BeautifulSoup(t, 'lxml')

new_urls = set()
#抽取a标记中的URL
links = soup.find_all('a', href=re.compile(r'/item'))#, recursive=True) #href=re.compile(r'\"/item/(.*?)\"'))
for link in links:
    print link
    with open("1.txt", 'a+') as f:
        f.write(str(link))
        f.write("\n")
