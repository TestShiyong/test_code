class Attribute:

    # def __init__(self):
    #     self.name = 'shiyong'

    # 访问不到属性时 调用此方法
    def __getattr__(self, item):
        print('调用了  __getattr__  方法')

    # 查找属性时调用此方法
    def __getattribute__(self, item):
        print('调用了 __getattribute__  方法')
        return super().__getattribute__(item)

    # 设置属性时 调用此方法
    def __setattr__(self, key, value):
        print('调用了  __setattr__   方法')
        if key == 'name':
            object.__setattr__(self, key, 'shiyong')
        else:
            object.__setattr__(self, key, value)

    # 删除属性时 调用了此方法
    def __delattr__(self, item):
        print(' 调用了  __delattr__  方法')
        if item == 'name':
            pass


attr = Attribute()
attr.name='shiyong'
attr.name='az'
print(attr.name)


print(attr.age)

del attr.name
print(attr.name)
