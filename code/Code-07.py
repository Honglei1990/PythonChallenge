# -*- coding: utf-8 -*-
'''
第 07 题
url：http://www.pythonchallenge.com/pc/def/oxygen.html
这一题的提示非常少，一张png格式图片
源代码标题  smarty
尝试单独解析图片

from PIL import Image
import re

image = Image.open('oxygen.png')
print('图片的宽和高：', image.size)
# 图片的宽和高 是  (629, 95)
x, y = (0, 0)
# x, y  这个图片的左上角第一个点
color = image.getpixel((x, y))
# color 是获取像素点的 RGBA 值，红R:, 绿G:, 蓝B:, 透明A:的一个元组，color 元组 (79, 92, 23, 255)，getpixel获取像素点
# 图片的中间一条横线 是灰黑色区域，除了这些区域其他看起来都是正常的.通过 RGBA 取色,分离 灰黑色区域和正常区域

打印马赛克区域
width, height = image.size
for i in range(width):
    for j in range(height):
        r,g,b,a = image.getpixel((i, j))
        if r == g == b:
            image.putpixel((i, j), (r, 0, 0, a))
        else:
            image.putpixel((i, j), (0, 0, 0, a))

# 计算马赛克区域的高度 和 颜色相同区域像素间隔
height_list = []
width_num = 0
width, height = image.size
# 创建循环查找中间 马赛克 height 数据，然后取其中一个
for i in range(width):
    for j in range(height):
        r, g, b, a = image.getpixel((i, j))
        if r == g == b:
            height_list.append(j)
            width_num = i

count_p_list = set(height_list)
for i in count_p_list:
    print('{}出现的次数是{}'.format(i, height_list.count(i)))
# 43 - 51 之间所有 都是中间马赛克 height 随便取一个即可 ，取 43值, width_num 的值是图片最后赋值成功的 代表这个马赛克的宽
# print(width_num)
# 计算得出马赛克的 宽 ： 607， 高： 43

# 循环取值 马赛克中 height为47的每一个 r的值
pixel_x = []
for i in range(1, 610, 7):
    r, g, b, a = image.getpixel((i, 47))
    pixel_x.append(r)

# 每一个都是重复的，去除和前一个字符是重复的尝试,最后尝试有问题 取消此部分 ，像素间隔7
# new_pixel_x = []
# for i in range(1, len(pixel_x)):
#     if pixel_x[i] != pixel_x[i-1]:
#         new_pixel_x.append(pixel_x[i])

# 获得的这些数字是什么意思呢，因为 返回整数i对应的ASCII字符，取值范围[0, 255]之间的正数 可以获得一些字母，尝试chr
str1 = ''
for i in pixel_x:
    str1 += chr(i)
print(str1)
# 打印后结果 mart guy, you made it. the next level is [105, 10, 16, 101, 103, 14, 105, 16, 121]
str_list = re.findall('(\[.+\])', str1)[0]
python_list = eval(str_list)
result = ''.join(chr(i) for i in python_list)
print(result)
'''
# 最后精简代码后

from PIL import Image
import re

image = Image.open('oxygen.png')
width, height = image.size
pixel_list = [image.getpixel((i, 43))[0] for i in range(1, 610, 7)]
str1 = ''.join([chr(i) for i in pixel_list])
str_list = re.findall('(\[.+\])', str1)[0]
python_list = eval(str_list)
result = ''.join(chr(i) for i in python_list)
print('http://www.pythonchallenge.com/pc/def/{}.html'.format(result))