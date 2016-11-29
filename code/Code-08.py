# -*- coding:utf-8 -*-

'''
第 07 题
url：http://www.pythonchallenge.com/pc/def/integrity.html
一个蜜蜂猜谜的图片，提示英文：where is the missing link?
网页源代码：title: working hard?
其中还有 一些 coords="179,284,214,311,255,320,281,226,319,224,363,309...等等"
coords坐标，是蜜蜂的整个身体的坐标，坐标内可用鼠标点击 并弹出登陆用户名和密码的窗体
最后的注释
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

蜜蜂的英文是 bee，通过修改bee.html登陆尝试，提示英文 and she is BUSY.
修改busy.html 登陆 提示 all bees sound busy too.
...此时联想到 busy too == bz2
python3 使用bz2 来 压缩或解压缩  需要是二进制字符串才可以，所以字符串前边加上b 即可
bz2.compress  压缩
bz2.decompress 解压缩
'''
import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

# 通过 bz2 解析
user = bz2.decompress(un).decode('utf-8')
pwd = bz2.decompress(pw).decode(('utf-8'))
print('用户名：{}\n密码：{}'.format(user,pwd))
# 用户名：huge 密码：file
# 答案网址： http://www.pythonchallenge.com/pc/return/good.html