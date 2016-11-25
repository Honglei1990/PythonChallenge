# -*- coding: utf-8 -*-
'''
第 06 题
url：http://www.pythonchallenge.com/pc/def/channel.html
有一个按钮提示 Paypal 捐赠。图片一个裤子的图标
查看源代码提示 作者希望对 pythonchallenage 做出一些捐赠，想象一下作为解密游戏，是不是有其他玄机。 channel 管道。
源代码最上端显示 -  zip -- 是不是跟这个模块有关呢
事实证明捐赠的和本关游戏毫无关系
zip指向 html
<html> <!-- <-- zip -->
把channel 替换zip 登陆网页 提示 yes, find the zip.找到了它
然后尝试把html替换成zip，直接下载了一个zip解压包
利用zipfile模块解压缩zip读取文件，在最下边有一个 readme.text
readme提示
welcome to my zipped list.

hint1: start from 90052
hint2: answer is inside the zip

从文件90052开始，答案就在zip里面


import zipfile
import re

num = '90052'
z_file = zipfile.ZipFile('channel.zip')
def go_next(zfile, num):
    #循环读取zip里面的txt文件，取出文件名 递归调用，自己调用自己
    filename = num+'.txt'
    print(zfile.getinfo(filename).comment,)
    text1 = zfile.read(filename).decode('utf-8')
    num = ''.join(re.findall('Next nothing is (\d+)', text1))
    if num:
        go_next(zfile, num)

go_next(z_file, num)

#打印到最后提示收集注释  collect the comments 换另外一个方法 方便打印注释 collect
'''
import zipfile
import chardet
import re

z_file = zipfile.ZipFile('channel.zip')
print(chardet.detect(z_file.read('readme.txt')))
#输出文件后，前边带一个b，编码格式为ascii
#需要decode 转码为utf-8


#设置初始文件头文件名和存储注释的comments
num = '90052'
comments = ''
while num:
    filename = num+'.txt'
    text1 = z_file.read(filename).decode('utf-8')
    comments += (z_file.getinfo(filename).comment).decode('utf-8')
    # print(text1)
    num = ''.join(re.findall("Next nothing is (\d+)", text1))

print(comments)
#结果为  HOCKEY.html  但进入后 网页提示 it's in the air. look at the letters.
#它在空气中。看字母，返回结果查看 看字母的话原来是  oxygen（氧气）
#重新使用  oxygen.html 后进入下一题