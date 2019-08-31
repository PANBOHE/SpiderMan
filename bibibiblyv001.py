from pyquery import PyQuery as pq
import requests
import re

def getHtml(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
    }
    html=requests.get(url,headers,verify=False)
    return html.text

def getListUrl(txt):

    doc=pq(txt)

    items=doc('#app > div.b-page-body > div > div.rank-container > div.rank-body > div.rank-list-wrap > ul > li > div.content').items()

    list=[]

    for item in items:
        dic={}
        title=item.text()
        href=item.attr('href')
        dic[title]=href
        list.append(dic)
    return list

# =============================================================================
# def parse_get_url(txt):
# 
#       pattern=re.compile(r'window.__playinfo__={(.*?)}',re.S)
#       content=re.findall(pattern,txt)
#       #content是一个list
#       
#       print('这是content',content)
#       print
# #      print(content[-1])
#       print('这是一个完整的例子 \n')
#       p=re.compile(r'"href":"(.*?)",',re.S)
#       url=re.findall('href,content[0])
#       print(url)
#       return url
# =============================================================================

 

def save_toFile(txt):

    f=open("b站热门排行视频.txt",'a',encoding='utf-8')

    f.write(txt)

    f.write('\n')

    f.close()

if __name__ == '__main__':

    t=getHtml('https://www.bilibili.com/ranking?spm_id_from=333.334.banner_link.1')
    urls=getListUrl(t)
    for info in urls:
        for title in info:
            print(title,'其中一个 \n')
        print('*********')

