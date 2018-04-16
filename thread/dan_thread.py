import requests
import time

link_list = []
with open('url.txt','r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)
    start = time.time()
    i= 1
    for eachone in link_list:
        try:
            r = requests.get(eachone)
            print(i)
            print(r.status_code,eachone)
            i += 1
        except Exception as e:
            print('Error',e)
    end = time.time()
    print('串行的总时间为：',end-start)
