from pyquery import PyQuery as pq
import requests
# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)
# print(doc('li'))

# # URL 初始化 两种读取方式
# doc= pq(url='https://cuiqingcai.com')
# print(doc('title'))
# html = pq(requests.get('https://cuiqingcai.com').text)
# print(html('title'))
# # 文件初始化
# doc = pq(filename='demo.html')
# print(doc('li'))

# 基本CSS选择器
# print(doc('#container .list li'))
# print(type(doc('#container .list li')))

# 查找节点
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)
#
# lis = items.children('.active')
# print(type(lis))
# print(lis)

# 父节点
# items = doc('.list')
# container = items.parent()
# print(type(container))
# print(container)
# parents = items.parents()
# print(type(parents))
# print(parents)

# items = doc('#container')
# parent = items.parents('.wrap')
# print(parent)

# 兄弟节点
# li = doc('.list .item-0.active')
# print(li.siblings('.active'))

# 遍历
# li = doc('.item-0.active')
# print(li)
# print(str(li))
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li,type(li))

# 获取信息或者属性
# a = doc('.item-0.active a')
# print(a,type(a))
# print("Href :",a.attr('href'),a.attr.href)
# a = doc('.item-1.active a')
# print("Text :",a.text())

# 获取多个结果
# a = doc('a')
# print(a,type(a))
# print(a.attr('href'),a.attr.href)
# for item in a.items():
#     print(item.attr.href)

# 获取内容
# a = doc('.item-0.active a')
# print(a)
# print(a.text())
# print(a.html())
# li = doc('li')
# print(li.html())
# print(li.text())
# print(type(li.text()))

# 节点操作
# remove_class and add_class
# li = doc('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('actvie')
# print(li)
# # attr 、text、html
# li.attr('name','link')
# print(li)
# li.text('Changed item')
# print(li)
# li.html('<span>changed item</span>')
# print(li)

# remove
# html = '''
# <div class="wrap">
#     Hello, World
#     <p>This is a paragraph.</p>
#  </div>
# '''
# doc = pq(html)
# wrap = doc('.wrap')
# wrap.find('p').remove()
# print(wrap.text())

# 伪装类选择器
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print(li)
li = doc('li:gt(2)')
print(li)
li = doc('li:nth-child(2n)')
print(li)
li = doc('li:contains(second)')
print(li)