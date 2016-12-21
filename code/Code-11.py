# -*- coding:utf-8 -*-

'''
第 07 题
url：http://www.pythonchallenge.com/pc/return/5808.html
提示： odd even 和一张图片
无任何提示，只能通过一个图片寻找答案，可能需要PIL的Image模块 专门处理图片
'''
from PIL import Image
image = Image.open('Code-11_Image.jpg')
big = image.crop((0,0,10,5)).resize((1000,500))
#截取 10像素宽 5像素高的图片，进行resize放大
# big.show()
#放大后的图片可以发现是一个规则的深色和浅色的组合，浅色系列的就是图案本身，深色则代表其他含义（答案）


#创建一个坐标不是我们需要的像素点
# def is_not_a_hole((x,y)):
#      '''坐标像素点 宽x 高y
#      判断语句1
#       x%2 + y%2 == 1
#      偶数行偶数列 0 + 0 == 0
#      偶数行奇数列 0 + 1 == 1
#      奇数行奇数列 1 + 1 == 2
#      奇数列偶数行 1 + 0 == 1
#      判断语句2
#      x%2 ^ y%2 == 1
#      偶数行偶数列 0 ^ 0 == 0
#      偶数行奇数列 0 ^ 1 == 1
#      奇数行奇数列 1 ^ 1 == 0
#      奇数列偶数行 1 ^ 0 == 1
#      '''
#      return x%2 ^ y%2

def is_not_a_hole(t):
    # 有一些问题存在  方法创建时无法 在位置t那里 插入 (x, y) 提示SyntaxError: invalid syntax 缩进错误
    x = t[0]
    y = t[1]
    #  return x&2 ^ y%2
    result = x%2 ^ y%2
    t = None
    return result

# python 3 方法中无法插入 tuple？    提示缩进错误
#测试一下 函数
# for i in [(0,3), (3,7), (2,6), (4,9)]:
#     print(i,'不是孔' if is_not_a_hole(i) else '是孔')
# big.show()
width, height = image.size
for i in range(width):
    for j in range(height):
        # if is_not_a_hole((i, j)):
        if i % 2 ^ j % 2:
            image.putpixel((i, j), (0, 0, 0))
image.show()
# 最后循环 修改不是孔的点为透明，show图像后，可以看到 evil 英文，使用  evil.html 后进入下一题
