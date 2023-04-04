#:@ TIME 2021/12/27   16:12
#:@FILE  re模块.py
#:@EMAIL  1557225637@QQ.COM
c="商品号：SP10278Special SP1022Occasion Dresses SP Cabernet #5c2c35   1"
# b=c.find('/')
# print(b)
# print(c[0:b])
aa='"code": 0,"error": "ccc"'

import re
#模块
print(re.findall('"code": (.*)?', aa))

#大写字母[A-Z],小写字母[a-z]
print(re.findall("[A-Z]+[\d]+",c))
#匹配所有数字 每个数字独立
print(re.findall("[\d]",c))
#匹配所有数字 集合+
print(re.findall("[\d]+", c))

#匹配所有字母 每个字母独立
# print(re.findall("[a-z]",c))
#匹配所有字母 集合+
# print(re.findall("[a-z+]",c))

#匹配字母+数字 字母和数字都独立
print(re.findall("[a-z'\d]']",c))

# print(re.findall("[A-Z]+[\d]+",c))