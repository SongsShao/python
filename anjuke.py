import requests
from bs4 import BeautifulSoup
for j in range(1,20):
    print('第%d页信息爬取中...' %int(j))
    link = "https://xa.anjuke.com/sale/p"+str(j)

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
             '(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

    r = requests.get(link,headers=header)
    soup = BeautifulSoup(r.text,'lxml')
    house_list = soup.find_all('li',class_="list-item")

    for house in house_list:
        name = house.find('div',class_="house-title").a.text.strip()
        price = house.find('span',class_="price-det").text.strip()
        price_area = house.find('span',class_="unit-price").text.strip()
        no_home = house.find('div',class_="details-item").span.text.strip()
        area = house.find('div',class_="details-item").contents[3].text
        floor = house.find('div',class_="details-item").contents[5].text
        year = house.find('div',class_="details-item").contents[7].text
        borker = house.find('span',class_="brokername").text.strip()
        borker = borker[1:]
        address = address.replace('\xa0\xa0\n                    ',' ')
        address = house.find('span',class_="comm-address").text.strip()
        tag_list = house.find_all('div',class_="tags-bottom")
        tags = [i.text for i in tag_list]

        print('房屋名称：',name,'价格：',price,'均价：',price_area,'几室几厅：',no_home,'面积：',area
              ,'\n层数：',floor,'建造年份：',year,'中介：',borker,'地址：',address,'标签：',tags)