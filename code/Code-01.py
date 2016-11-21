# -*- coding: utf-8 -*-
'''
第 1 题
url：http://www.pythonchallenge.com/pc/def/map.html
tips：everybody thinks twice before solving this.
str： g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
根据图片 K → M, O → Q, E → G
得知左右字母向后顺延两位
'''
abc1 = 'abcdefghijklmnopqrstuvwxyz'
abc2 = 'cdefghijklmnopqrstuvwxyzab'
str_maketrans = str.maketrans(abc1,abc2)
str1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = str1.translate(str_maketrans)
print(result)
#result =  i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
# 结果说明 同样适用于 现在的网址，尝试一下
url = 'http://www.pythonchallenge.com/pc/def/map.html'
print(url.translate(str_maketrans))
#看来不是所有都修改，只修改html部分尝试
new_url = 'http://www.pythonchallenge.com/pc/def/{}.html'.format('map'.translate(str_maketrans))
print(new_url)
#结果正确 第2题 网址是：http://www.pythonchallenge.com/pc/def/ocr.html
#运用 maketrans 和 translate 函数