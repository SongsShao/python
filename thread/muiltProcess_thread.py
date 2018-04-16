from multiprocessing import Process,Queue
import requests
import time

link_list = []
with open('url.txt','r') as file:
    file_list = file.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q = q
    def run(self):
        print('Starting ',self.pid)
        while not self.q.empty():
            crawler(self.q)
        print('Exiting ',self.pid)
def crawler(q):
    url = q.get(timeout=2)
    try:
        r = requests.get(url,timeout=20)
        print(q.qsize(),r.status_code,url)
    except Exception as e:
        print(q.qsize(),url,'Error: ',e)

if __name__ == '__main__':
    ProcessName = ["Process-1","Process-2","Process-3"]
    workQueue = Queue(300)
    for url  in link_list:
        workQueue.put(url)
    for i in range(4):
        p = MyProcess(workQueue)
        p.daemon = True
        p.start()
        p.join()

    end = time.time()
    print("Process+Queue多线程爬虫总的时间：",end-start)
    print("Exiting Main Thread!")