# -*- coding: utf-8 -*-
'''
第 03 题
url：http://www.pythonchallenge.com/pc/def/equality.html
tips：One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
(一封小信，周围有三个大保镖，两边各有一个。)一个小写字母 旁边三个大写字母
源代码网页有一些大小写英文随机组合,详情在Code-03.txt
'''
#使用正则表达式
'''
import re
text = open("Code-03.txt", 'r').read()
new_text = text
list1 = []
index = 0
# 创建符合的条件语句，patten1 完全符合 三个大写字母和一个小写字母组合，而不是四个大写字母或换行符的存在
patten1 = re.compile('[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]')
patten2 = re.compile('[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z]\s')
patten3 = re.compile('\s[A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]')
# while循环查找符合的值 给list1
while index < len(new_text)-8:
    if re.search(patten1,new_text[index:index+9]):
        print(index, new_text[index:index+9])
        list1.append(new_text[index:index+9])
        index += 9
    elif re.search(patten2,new_text[index:index+9]):
        print(index, new_text[index:index+9])
        list1.append(new_text[index:index+9])
        index += 9
    elif re.search(patten3,new_text[index:index+9]):
        print(index, new_text[index:index+9])
        list1.append(new_text[index:index+9])
        index += 9
    else:
        index += 1
print('\n'.join(list1))
str1 = ''
# 循环取值最小字母 生成新链接
for s in list1:
    str1+=s[4]
url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format(str1)
print(url)
# 使用 正则表达式 re，实例化 compile方法和 search方法
'''
# 拒绝暴力循环取值
import re
text = open("Code-03.txt", 'r').read()
# 核心内容 正则表达式 '^' 非，'()' 取值范围 ，'{3}'重复3次
pattern = '[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]'
result = re.findall(pattern,text)
url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format(''.join(result))
print(url)

