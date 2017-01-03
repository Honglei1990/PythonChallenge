# -*- coding: utf-8 -*-
'''
第 05 题
author: Honglei1990
url：http://www.pythonchallenge.com/pc/def/peak.html
tips：查看网页源代码 有一个  peakhell 标签  src=‘banner.p’
进入banner.p 是混乱的txt字符，先读取数据尝试
http://www.pythonchallenge.com/pc/def/banner.p
'''

'''
根据网页源代码 title  pickhell 自定义标签 pickhell  和 图片下的提示 pronounce it ,可以联想到
内置模块  pickle
pickle.dump(obj, file[, protocol])
　　序列化对象，并将结果数据流写入到文件对象中。参数protocol是序列化模式，默认值为0，表示以文本的形式序列化。
protocol的值还可以是1或2，表示以二进制的形式序列化。

------------------------------------------
pickle.load(file)
　　反序列化对象。将文件中的数据解析为一个Python对象。
'''

import pickle
import urllib.request

url = 'http://www.pythonchallenge.com/pc/def/banner.p'
datafile = urllib.request.urlopen(url)
content = pickle.load(datafile)

def parse_content(line):
    str1 = ''
    for char, times in line:
        str1 += char * times
    return str1
for line in content:
    print(parse_content(line))

#结果出现在眼前