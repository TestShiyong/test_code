''' 限制实例属性 节约内存'''
class A:
    __slots__ = ['name']


a=A()
a.name='shiyong'
a.age='100'