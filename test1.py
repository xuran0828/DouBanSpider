# encoding:utf-8
import urllib.request
import re


# 获取单个电影链接里的内容，比如评分，剧情简介
def get_score_information(link):
    html = urllib.request.urlopen(link)
    html = html.read().decode("utf-8")

    score_patten = re.compile(r'<strong class=".*" property=".*">(.*)</strong>')
    score_all = re.findall(score_patten, html)
    for score in score_all:
        print("The movie score is :" + score)


count = 1
url = "https://movie.douban.com/top250?start="
#urls = [url + str(num * 25) for num in range(2)] # 列表推导式
urls=[]
for num in range(2):
    urls.append(url+str(num*25))
for one in urls:
    html = urllib.request.urlopen(one)
    html = html.read().decode("utf-8")
    # 提取电影名称的正则表达式
    title_patten = re.compile(r'<span class="title">(.*?)</span>')
    # 提取电影链接内容的正式表达式
    link_patten = re.compile(r'<a href="(.*?)" class="">')
    title_all = re.findall(title_patten, html)
    link_all = re.findall(link_patten, html)
    # 因为得到的电影名称有其它格式的存在，需要清洗整理到新的列表
    title_arr = []
    for each in title_all:
        if each.find('/') == -1:
            title_arr.append(each)
    for title, link in zip(title_arr, link_all):
        print("Top " + str(count) + ": " + title + "   link:   " + link)
        get_score_information(link)
        count += 1