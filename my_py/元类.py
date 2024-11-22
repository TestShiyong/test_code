
"""
自定义元类
指定元类后 会先把当前类加载完成 然后把当前类 anme 属性 方法 传入元类new方法参数 通过type 创建类，重写new方法
类名 属性 方法 当做入参  return 返回

"""
# 自定义元类 必须继承type类
class MyTest(type):
    def __new__(cls, name, base, attrs, *args, **kwargs):
        print('自定义元类')
        print(attrs)
        return super().__new__(cls, name, base, attrs)


# 指定元类后 会先把当前类加载完成 然后把当前类 anme 属性 方法 传入元类new方法参数 创建类 r
class Test(metaclass=MyTest):
    aa='shiyong'
    def eat(self):
        print('吃吃吃')

# test=Test()
# aa = MyTest('mytest', (object,), {'shiyong': 200})