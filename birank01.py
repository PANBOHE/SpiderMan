# -*- coding: utf-8 -*-

"""

Created on Fri Aug 30 15:46:43 2019

@author: hepanbo

E-mail: panbohero@126.com

day day up up!

"""

import json
from bs4 import BeautifulSoup
from urllib import request

            
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  '(KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}        

url='https://www.bilibili.com/ranking?spm_id_from=333.334.banner_link.1'
req = request.Request(url, headers = headers)    
response = request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html, 'lxml')
#�ҵ�����<ul class='rank-list'>
dic = {}
#��֪��Ϊʲô��img��src������������
# =============================================================================
# list = soup.find_all('div',attrs={'class':'lazy-img cover'})
# print(list)
# =============================================================================
#list = soup.find_all('ul',attrs={'class':'rank-list'})

# =============================================================================
# #�������
# for paiming in soup.find_all('div',attrs={'class':'num'}):
#     print('paimingshi:\n',paiming.get_text())
#     
# =============================================================================
# =============================================================================
# 
# #img��ò���
# for img in soup.find_all('div',attrs={'class':'lazy-img cover'}):
#     print('paimingshi:\n',img)
# =============================================================================

# =============================================================================
# 
# #������֣��������  ����������//xxxxxxx/  �ǵ�ȥ��
# for info in soup.find_all('a',attrs={'class':'title'}):
#     print('paimingshi:\n',info.get('href'),'\n',info.get_text())
# =============================================================================
    
# =============================================================================
# for bofang in soup.find_all('div',attrs={'class':'detail'}):
#     
#     print('bofang:\n',bofang)
#     
# =============================================================================
    
    
lis= soup.select('#app > div.b-page-body > div > div.rank-container > div.rank-body > div.rank-list-wrap > ul > li > div.content ')
for l in lis:    
    str =l.select('div a')[0]['href']
    str1=str[2:-1]
    print("������URL��ַ�ǣ�",str1)
    name =l.select('div a')[1].get_text()
    print('��������Ƶ�����ǣ�',name)
    bfl=l.select('div span')[0].get_text()
    sc=l.select('div span')[1].get_text()
    zz=l.select('div span')[2].get_text()
    print("������Ϊ:",bfl)
    print("�ղ���Ϊ��", sc)
    print('����������:',zz)
    print('****************')
# =============================================================================
# for content in list:
#     print(content)
# # =============================================================================
# #     paiming=content.findall('div',attrs={'class':'num'})
# #     print('paiming ��:', paiming.get_text(),'\n')
# # =============================================================================
#     print('***********************************')
# =============================================================================
    
