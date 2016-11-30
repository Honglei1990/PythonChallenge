# -*- coding:utf-8 -*-

'''
第 07 题
url：http://www.pythonchallenge.com/pc/return/bull.html
页面提示 ：len(a[30]) = ?
点击公牛 出现 sequence.txt 页面  提示： a = [1, 11, 21, 1211, 111221,
源代码 title ： what are you looking at?
a[0] = 1, a[1] = 11, a[2] = 21, a[3] = 1211, a[4] = 111221
'''
#想法1 ，无视列表值本身，根据len(a[1]) + len(a[2]) = len(a[3])直接计算第30个的长度
# result = [1, 2, 2, 4, 6]
# for i in range(26):
#     result.append(result[-1]+result[-2])
# print(result[30])
#使用答案 1664080.html 无法进入 ，似乎是错误的 ，重新来过

# 想法2， 想出值是如何产生的，并根据值来计算长度
# a[0] = 1 ,    1个1    结果是  11
# a[1] = 11,    2个1    结果是  21
# a[2] = 21,    1个2 1个1    结果是 1211
# a[3] = 1211,  1个1 1个2 2个1 结果是 111221
# a[4] 111221   3个1 2个2 1个1  结果是 312211
# a[5] 212211   1个2 1个1 2个2 2个1 结果是 12112221
# 根据以上 编写 一个数据结构算法
def getNext(number):
    CureentNum = number[0]    # 把number第一个数赋值给当前数CureentNum
    CountNum = 1              # 计算次数的变量
    resultNum = ''            # 存放结果的变量

    for i in number[1:]:
        if CureentNum == i:
            CountNum += 1
        else:
            resultNum += str(CountNum) + CureentNum
            CureentNum = i
            CountNum = 1
    resultNum += str(CountNum) + CureentNum
    return resultNum

a = '1'
for i in range(30):
    a = getNext(a)
print(len(a))
# http://www.pythonchallenge.com/pc/return/5808.html