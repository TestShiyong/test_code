"""
1.数据类型
2.运算符
3.转义符
4.切片
"""

"""
可变函数和不可变类型
不可变：对象所指向不可以改变
不可变的类型： int  str  float  tuple
可变类型：对象所指向的内存中的值是可以改变的
类型：dict  list

"""

# 运算符
# 除
print(5 / 2)

# 整除
print(10 // 6)

# 取模
print(11 % 3)

# 次方
print(10 ** 9)

# 转义符
print('hello 1\nhello2\nhello3\nhello4')  # ”转义符\n的使用“直接\n换行

print('hello 1\thello2\thello3\thello4')  # ”转义符\t的使用“\t相当于四个空格键

print('hello 1\rhello2\rhello3\thello4')  # ”转义符\r的使用“\r前面的所有代码不输出

print('hello11\b\thello22\thello33\thello44')  # ”转义符\b的使用“\r前面一格的代码不输出

print('http:\\\\www.baidu.com')  # 输出网址双斜杠时要多加两个斜杠

print('老师说：\'你们好\'')  # 输出引号要用到斜杠

# 使用原本的字符  不希望字符串中的转义符起到作用，就使用原字符，在字符串之前加上r或R
print(r'hello 1\nhello2\nhello3\nhello4')  # 字符串之前加r，让字符串中的转义符失效

# 切片
a = ('123456789')
print(a[2])
print(a[6])
print(a[-3])
print(a[0:6])
print(a[0:-4])
print(a[-9:-3])
print(a[-3:5])
print(a.count("6"), "统计字符串内有几个6")
print(len(a), "获取字符串的长度")  # ,''
print(a.find("7"), "获取该字符串左边的字符串")
print(a.index("3"), "获取该字符串的坐标")
print(a[0:])
3
7
7
123456
12345
123456
