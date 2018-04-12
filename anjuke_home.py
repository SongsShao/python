import requests
from bs4 import BeautifulSoup
for j in range(1,3):
    print('第%d页信息爬取中...' %int(j))
    link = "https://xa.anjuke.com/prop/view/A1167845946?from=filter&" \
           "spread=commsearch_p&position="+str(j)+'&kwtype=filter&now_time=1522672868'

    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
             '(KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}

    r = requests.get(link,headers=header)
    soup = BeautifulSoup(r.text,'lxml')
    details_list = soup.select('div.first-col.detail-col > dl > dd')
    name = details_list[0].get_text().replace('\n','')
    address = details_list[1].get_text().replace('\n							','')[1:-3]
    year = details_list[2].get_text()
    types = details_list[3].get_text()
    house_list = soup.select('div.second-col.detail-col > dl > dd')
    house_type = house_list[0].get_text().replace('\n					','')[:6]
    area = house_list[1].get_text()
    direction = house_list[2].get_text()
    floor = house_list[3].get_text()
    price_list = soup.select('div.third-col.detail-col > dl > dd')
    decoration = price_list[0].get_text()
    unit_price = price_list[1].get_text()
    down_payment = price_list[2].get_text().replace('\n					','')[:6]
    monthly_supply = price_list[3].get_text()
    # with open('E:\\py\\anjuke.txt', 'a+') as f:
    #     f.write('所属小区：',name,'所在位置：',address,'建造年代：',year,'房屋年代：',types,
    #       '\n房屋户型：',house_type,'建筑面积：',area,'房屋朝向：',direction,'所在楼层：',floor,
    #       '\n装修程度：',decoration,'房屋单价：',unit_price,'参考首付：',down_payment,'参考月供：',monthly_supply)
    #     f.close()

    print('所属小区：',name,'所在位置：',address,'建造年代：',year,'房屋年代：',types,
          '\n房屋户型：',house_type,'建筑面积：',area,'房屋朝向：',direction,'所在楼层：',floor,
          '\n装修程度：',decoration,'房屋单价：',unit_price,'参考首付：',down_payment,'参考月供：',monthly_supply)