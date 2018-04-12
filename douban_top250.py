import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                ' (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
               'Host':'movie.douban.com'}
    movie_list = []
    movie_listD = []
    for i  in range(0,10):
        link = 'https://movie.douban.com/top250?start='+str(i*25)+'&filter='
        r = requests.get(link,headers=headers,timeout=10)
        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.find_all('div',class_='info')
        for each in div_list:
            movie = each.div.a.text.strip()
            # movieD = each.div.p.text.strip()
            movie_list.append('电影名：'+movie)
        # for each in div_listD:
        #     movieD = each.p.text.strip()
        #     movie_listD.append(movieD)
    return movie_list

movies = get_movies()
print(movies)