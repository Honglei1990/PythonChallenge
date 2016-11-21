# -*- coding: utf-8 -*-
'''
第 02 题
url：http://www.pythonchallenge.com/pc/def/ocr.html
tips：recognize the characters. maybe they are in the book, but MAYBE they are in the page source.
find rare characters in the mess below:
'''
# 提前把网页源代码混乱字符放到 Code-02.txt中
text1 = open('Code-02.txt')
characters = text1.read()
# print(len(characters)) 98764个字符
#创建一个去重复对象 abc
abc = set(characters)
#使用set方法 虽然非常方便，但顺序会变，导致无法分析最后结果，, 所以尝试abc1  列表循环判断取值
abc1 = []
for i in characters:
    if i not in abc1:
        abc1.append(i)
# 创建一个列表 counts 存放 字符和字符个数
counts = []
for i in abc1:
    counts.append((i,characters.count(i)))
#print counts 可以发现 不重复的字符 只有 1 次，所以创建一个判断 把等于1的 取出来
str1 = ''
for str, count in counts:
    if count == 1:
        str1 += str

url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format(str1)
print(url)
#最终打印出下一页url，过关
#运用 count函数计算数量
# http://www.pythonchallenge.com/pc/def/equality.html