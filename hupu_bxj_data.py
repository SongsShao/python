import requests
from bs4 import BeautifulSoup
import datetime
import MySQLdb
import time

def get_page(link):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64;x64;rv:59.0) Gecko/20100101 Firefox/59.0'}
    r = requests.get(link,headers=headers)
    html = r.content
    html = html.decode('UTF-8')
    soup = BeautifulSoup(html,'lxml')
    return soup

def get_data(post_list):
    data_list=[]
    for post in post_list:
        title_id = post.find('div',class_='titlelink box')
        title = title_id.a.text.strip()
        post_link = title_id.a['href']
        post_link = 'https://bbs.hupu.com'+post_link

        #作者、作者链接、创建时间
        author_div = post.find('div',class_='author box')
        author = author_div.find('a',class_='aulink').text.strip()
        author_page = author_div.find('a',class_='aulink')['href']
        start_data = author_div.select('a:nth-of-type(2)')[0].get_text()
        #回复人数和浏览次数
        reply_view = post.find('span',class_='ansour box').text.strip()
        reply = reply_view.split('/')[0].strip()
        view = reply_view.split('/')[1].strip()
        #最后回复用户和最后回复时间
        reply_div = post.find('div',class_='endreply box')
        reply_time = reply_div.a.text.strip()
        last_reply = reply_div.find('span',class_='endauthor').text.strip()
        if ':' in reply_time:
            date_time = str(datetime.date.today())+' '+ reply_time
            date_time = datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M')
        else:
            date_time = datetime.datetime.strptime(reply_time,'%Y-%m-%d').date()
        data_list.append([title,post_link,author,author_page,start_data,reply,view,last_reply,date_time])
    return data_list

class MysqlAPI(object):
    def __init__(self,db_ip,db_name,db_password,table_name,db_charset):
        self.db_ip = db_ip
        self.db_name = db_name
        self.db_password = db_password
        self.table_name = table_name
        self.db_charset = db_charset
        self.conn = MySQLdb.connect(host=self.db_ip,user=self.db_name,
                                    password=self.db_password,db=self.table_name,charset=self.db_charset)
        self.cur = self.conn.cursor()
    def add(self,title,post_link,author,author_page,start_data,reply,view,last_reply,date_time):
        sql = "INSERT INTO hupu(title,post_link,author,author_page,start_data,reply,view,last_reply,date_time)"\
                                   "VALUES (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')"

        self.cur.execute(sql %(title,post_link,author,author_page,start_data,reply,view,last_reply,date_time))
        self.conn.commit()

for i in range(1,3):
    link = 'http://bbs.hupu.com/bxj-'+str(i)
    print('开始第%s页数据爬取...' %i)
    soup = get_page(link)
    soup = soup.find('div',class_='show-list')
    post_list = soup.find_all('li')
    data_list = get_data(post_list)
    hupu_post = MysqlAPI('localhost','root','mysql','scraping','utf8')
    for each in data_list:
        hupu_post.add(each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7],each[8])
    print('第%s页爬取完成！' %i)
    time.sleep(3)