# -*- coding: utf-8 -*-
'''
第 04 题
url：http://www.pythonchallenge.com/pc/def/linkedlist.php
tips：点击图片 进入一个网址 后缀名为 linkedlist.php?nothing=12345
文本信息提示 and the next nothing is 44827，链接赋值后进入下一个网页 依然提示
利用 requests 和 bs4 爬虫方式获取网页信息
'''
#
import requests
from bs4 import BeautifulSoup

number = '12345'
count = 0
# 创建循环 获取数据
while True:
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(number)
    try:
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        title = soup.select('body')[0].text
        number = title.split()[-1]
        a = int(number)
        count += 1
        print(url, '\t', title, '第{}次进入网页'.format(count))
    except Exception as e:
        with open('Exception_code.txt', 'a+') as file1:
            text1 = 'site_content:'+'\t'+title+'第{}次进入网页'.format(count)+'\n'
            file1.write(text1)

# 通过 Exception_code 获取 最后的 html是peak.html
# 结果 http://www.pythonchallenge.com/pc/def/peak.html