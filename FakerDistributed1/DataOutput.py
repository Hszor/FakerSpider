# _*_coding:utf-8 _*_
import codecs


def safe_str(obj):
    try:
        return str(obj)
    except UnicodeEncodeError:
        return obj.encode('utf-8', 'ignore')
    return ""

class DataOutput(object):
    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def datas_size(self):
        return len(self.datas)

    def output_html(self):
        fout = codecs.open('baike.html', 'w+', encoding='utf-8')
        fout.write("<html>")
        fout.write("<meta charset='UTF-8'>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            # fout.write("<td>%s</td>" % data['url'])
            # fout.write("<td>%s</td>" % data['title'])
            # fout.write("<td>%s</td>" % data['summary'])
            print "d::", data['url']
            print "d::", data['title']
            print "d::", data['summary']
            fout.write("<td>{}</td>".format(data['url'].strip()))
            fout.write("<td>{}</td>".format(data['title'].strip()))
            fout.write("<td>{}</td>".format(data['summary'].strip()))
            fout.write("</tr>")
        #清空列表，减小内存占据
        self.datas = []
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()


