from urllib import request
from lxml import etree

# coding=gbk
def crow(i):
    url='https://movie.douban.com?start='+str(5*i)
    html=request.urlopen(url).read()
    html=etree.HTML(html)
    datas = html.xpath('div/div[@class="s"]')
    a=0
    for data in datas:
        data_title=data.xpath('p/text()')
        data_info=data.xpath('div/div[2]/div[@class="bd"]/p[1]/text()')
        data_quote=data.xpath('div/div[2]/div[@class="bd"]/p[2]/span/text()')
        data_score=data.xpath('p/strong/text()')
        data_num=data.xpath('div/div[2]/div[@class="bd"]/div/span[4]/text()')
        data_picurl=data.xpath('div[@class="cover-wp"]/img/@src')
        print("No: "+str(i*20+a+1))
        print(data_title)
        with open('movie.txt','a+',encoding='utf-8')as f:
            picname = 'c:/top250/' + str(i * 20 + a + 1) + '.jpg'
            f.write("No: "+str(i*20+a+1)+'\n')
            f.write(data_title[0]+'\n')
            f.write(str(data_info[0]).strip()+'\n')
            f.write(str(data_info[1]).strip()+'\n')
            if data_quote:
                f.write(data_quote[0]+'\n')
            f.write(data_score[0]+'\n')
            f.write(data_num[0]+'\n')
            f.write('\n'*3)
            request.urlretrieve(data_picurl[0],filename=picname)
        a+=1
for i in range(10):
    crow(i)