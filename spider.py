#coding=utf-8


#str通过encode()方法可以编码为指定的bytes。
# 反过来，当从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
# 要把bytes变为str，就需要用decode()方法。
# 反之，则使用encode()方法即可！
import requests
from bs4 import BeautifulSoup

resp=requests.get('https://www.baidu.com') #请求百度首页
resp.encoding='gbk'
print (resp) #打印请求结果的状态码
print (resp.content) #打印请求到的网页源码

bsobj=BeautifulSoup(resp.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
a_list=bsobj.find_all('a') #获取网页中的所有a标签对象
#text='' # 创建一个空字符串
text=[]#创建一个列表
for a in a_list:
    href=a.get('href') #获取a标签对象的href属性，即这个对象指向的链接地址
    text.append(href)
    #text+=href+'\n' #加入到字符串中，并换行
with open('url.txt','w') as f: #在当前路径下，以写的方式打开一个名为'url.txt'，如果不存在则创建
    f.write(str(text)) #将text里的数据写入到文本中，当创建一个列表的时候，注意test要转换成str类型