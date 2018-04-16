import gevent
from gevent.queue import Queue,Empty
import requests
import time
from bs4 import BeautifulSoup

from gevent import monkey
monkey.patch_all()

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
             '(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

link_list = []
with open('url.txt','r') as file:
    file_list = file.readlines()
    for i in file_list:
        link = i.split("\t")[1]
        link = link.replace("\n","")
        link_list.append(link)
start = time.time()

def crawler(index):
    Process_id = 'Process-' + str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        try:
            r = requests.get(url,timeout=20)
            html = r.content
            html = html.decode("UTF-8")
            soup = BeautifulSoup(html,'lxml')
            title = soup.select('title')[0].get_text()
            print(Process_id,workQueue.qsize(),r.status_code,url,title)
        except Exception as e:
            print(Process_id,workQueue.qsize(),url,"Error :",e)

def boss():
    for url in link_list:
        workQueue.put_nowait(url)

if __name__ == '__main__':
    workQueue = Queue(300) #设置工作区间要进行处理数据的条数
    gevent.spawn(boss).join()
    jobs = []
    for i in range(10):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)
    end = time.time()
    print("gevent+Queue多协议爬虫的总时间为：",end-start)
    print("Main Ended!")

