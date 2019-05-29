import requests, sys, time
from bs4 import BeautifulSoup
# if __name__ == '__main__':
    #每一章内容
    # target = 'http://www.biqukan.com/1_1094/5403177.html'
    # req = requests.get(url=target)
    # html = req.text
    # bf = BeautifulSoup(html, features='html5lib')
    # texts = bf.find_all('div', class_='showtxt')
    # print(texts[0].text.replace('\xa0'*8,'\n\n'))

    #各个章节名字
    # target = 'http://www.biqukan.com/1_1094/'
    # req = requests.get(url=target)
    # html = req.text
    # div_bf = BeautifulSoup(html, features='html5lib')
    # div = div_bf.find_all('div', class_='listmain')
    # print(div[0])

    #每个章节链接
    # server = 'http://www.biqukan.com/'
    # target = 'http://www.biqukan.com/1_1094/'
    # req = requests.get(url = target)
    # html = req.text
    # div_bf = BeautifulSoup(html, features='html5lib')
    # div = div_bf.find_all('div', class_='listmain')
    # a_bf = BeautifulSoup(str(div[0]), features='html5lib')
    # a = a_bf.find_all('a')
    # for each in a:
    #     print(each.string, server + each.get('href'))

class downloader(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        self.name = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url=self.target)
        html = req.text
        div_bf = BeautifulSoup(html, features='html5lib')
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]), features='html5lib')
        a = a_bf.find_all('a')
        self.nums = len(a[15:])
        for each in a[15:]:
            self.name.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self,target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, features='html5lib')
        texts = bf.find_all('div',class_='showtxt')
        texts = texts[0].text.replace('\xa0'*8, '\n\n')
        return texts

    def writer(self,name, path, text):
        write_flag = True
        # with could create temporary operating environment
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name+'\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('Begining: ')
    for i in range(dl.nums):
        dl.writer(dl.name[i], 'novel.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("\r{1}".format('|', '%.3f%%' % float(i/dl.nums)))
        sys.stdout.flush()
    print('finished')
# for i in range(100):
#     percent = i / 100
#     sys.stdout.write("\r{1}".format('|'*i,'%.2f%%' % (percent * 100)))
#     sys.stdout.flush()
#     time.sleep(0.1)

