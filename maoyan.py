import requests
from requests.exceptions import RequestException
import re
import json
def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None
def parse_one_page(html):
    pattern=re.compile('<dd.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a.*?>(.*?)'
                       +'</a>.*?releasetime">(.*?)</p>'
                       +'.*?star">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2],
            'time':item[3].strip()[5:],
            'actor':item[4].strip()[3:],
            'score':item[5]+item[6],
        }
def write_to_page(content):
    with open('result.txt', 'a+', encoding='utf-8')as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()
def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_page(item)



if __name__=='__main__':
    for i in range(10):
	    main(i*10)

