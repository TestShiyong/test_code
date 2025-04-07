"""
dict
字典
"""
# 定义：Python字典是一种可变容器模型，且可存储任意类型对象，如字符串、数字、元组等其他容器模型。

# 字典的每个键值key=>value对用冒号 : 分割，每个对之间用逗号,分割，整个字典包括在花括号{}中 ,格式如下所示：

# 常用get查找

# dict内置函数
# 增加：dict={}  修改 dict{key}=value
# 删除：dict,Pop , dict.popitem()   dict.clear
# 查：items（） values（）  keys（）


a = {}  # 定义空列表
print(type(a))  # 输出字典类  dict     <class 'dict'>

# 字典增加元素
a['手机品牌'] = '华为'
a['价格'] = '999'
a['型号'] = 'mate30'
a['颜色'] = 'red'
print(a)
# {'手机品牌': '华为', '价格': '999', '型号': 'mate30', '颜色': 'red'}

# For循环便利字典,只输出k值
# 尝试便利字典 ，便利的结果只有key
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
for i in dict1:
    print(i)
# 石头
# 月月
# 小王
# 小红


# items()  # 字典转元组
# 函数items  字典转元组
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print(dict1.items())
# dict_items([('石头', 99), ('月月', 88), ('小王', 22), ('小红', 78)])


# 通过items 转元组 便利，通过元组的下标值做判断
for n in dict1.items():
    print(n)
    if n[1] > 80:
        print(n[1])
# ('石头', 99)
# 99
# ('月月', 88)
# 88
# ('小王', 22)
# ('小红', 78)
 
# items()转元组后 拆包(字典)，赋值给变量
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
for a, b in dict1.items():
    print(a, b)
# 石头 99
# 月月 88
# 小王 22
# 小红 78


# 函数values
# 转元组包列表，只输出values值
# 函数values
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
# 输出字典的values
print(dict1.values())
# dict_values([99, 88, 22, 78])


# For循环 用values便利 值
# 便利出 字典的vaules
for l in dict1.values():
    print(l)
# 99
# 88
# 22
# 78
#  
# keys（for便利key）

dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
for ll in dict1.keys():
    print(ll)

#
# 列表判断kye是否存在 用in
# 找人，找key  用in
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print('小红' in dict1)
# True


# 常用get函数，根据key查找值，如果key不存在就返回None
# 可以设定默认值，找不到就返回默认值
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print(dict1.get('我'))  # None
print(dict1.get('我', '默认值'))  # 默认值
print(dict1.get('石头'))  # 99
# None
# 99


# 函数dict.fromkeys  将数据类型转成字典,添加默认值
jj = '啊'
ff = [1, 2, 3, 4, 5, 6, 7, 8]
p = dict.fromkeys(jj, '默认值')
b = dict.fromkeys(ff, '默认值')
print(p)
print(b)
# {'啊': '默认值'}
# {1: '默认值', 2: '默认值', 3: '默认值', 4: '默认值', 5: '默认值', 6: '默认值', 7: '默认值', 8: '默认值'}
#  
# 字典删除元素
# Del dict1[keyi]

dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
del dict1['石头']
print(dict1)
# {'月月': 88, '小王': 22, '小红': 78}


# pop  根据key 删除键值对,删除成功返回 键值对的值
# 字典删除元素  函数pop  根据key 删除键值对， 删除成功返回 键值对的值 ，
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print(dict1.pop('月月', '找不到要删除的key，默认值'))  # 找到返回 值
print(dict1.pop('是', '找不到要删除的key，默认值'))  # 找不到返回默认值
# 99
# 88
# 找不到要删除的key，默认值


# popitem()  #删除最后一建值对 做返回
# 删除字典末尾的键值对 函数 popitem()
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print(dict1.popitem())  # 删除最后一个值 做返回
# ('小红', 78)


# clear  清空字数据
# 函数 clear  清空字数据
dict1 = {'石头': 99, '月月': 88, '小王': 22, '小红': 78}
print(dict1.clear())
print(dict1)
# {}
