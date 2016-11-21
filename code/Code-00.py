# http://www.pythonchallenge.com/pc/def/0.html
# Hint: try to change the URL address.
# 提示尝试改变URL, 把0改成1后，进入到一个页面
# http://www.pythonchallenge.com/pc/def/1.html
# 提示 2**38 is much much larger.

url = 'http://www.pythonchallenge.com/pc/def/0.html'
num = 2**38
new_url = url.replace('0', str(num))
print(new_url)

# 结果是 http://www.pythonchallenge.com/pc/def/274877906944.html
# 成功进入下一题
