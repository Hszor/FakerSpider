# _*_coding:utf-8 _*_
import re
import urlparse
from bs4 import BeautifulSoup


class HTMLParse(object):

    def parser(self, page_url, html_content):
        '''
        解析网页内容，抽取其中的URL和数据
        :param page_url: 下载页面的URL
        :param html_content: 下载的网页内容
        :return:
        '''
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_url = self._get_new_url(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_url, new_data

    def _get_new_url(self, page_url, soup):
        '''
        获取页面中新的URL
        :param page_url:
        :param soup:
        :return:
        '''
        new_urls = set()
        #抽取a标记中的URL
        links = soup.find_all('a', recursive=True, href=re.compile(r'/item'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        # links = soup.find_all('a', recursive=True, href=re.compile(r'\"/item/(.*?)\"'))
        # for link in links:
        #     print "link::", link

        return new_urls

    def _get_new_data(self, page_url, soup):
        '''
        获取页面中需要提取的数据
        :param page_url:
        :param soup:
        :return:
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data

