from multiprocessing import Pool,Manager
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
def crawler(q,index):
    Process_id = 'Process-' + str(index)
    while not q.empty():
        url = q.get(timeout=2)
        try:
            r = requests.get(url,timeout=20)
            print(Process_id,q.qsize(),r.status_code,url)
        except Exception as e:
            print(Process_id,q.qsize(),url,'Error: ',e)

if __name__ == '__main__':
    managers = Manager()
    workQueue = managers.Queue(300)
    for url  in link_list:
        workQueue.put(url)
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(crawler,args=(workQueue,i))
    pool.close()
    pool.join()

    end = time.time()
    print("Pool+Queue多线程爬虫总的时间：",end-start)
    print("Exiting Main Thread!")