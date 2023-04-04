class M:

    def __get__(self, instance, owner):
        print('描述器对象访问属性时__get__ 方法被调用')
        print('self:', self)
        print('instance:', instance)
        print('owner;', owner)
        return self.value

    def __set__(self, instance, value):
        print('描述器对象设置属性时__set__ 方法被调用')
        print('self:', self)
        print('instance:', instance)
        print('value;', value)
        self.value = value

    def __delete__(self, instance):
        print('删除描述器对象时 __del__  方法被调用 ')
        self.value = None


class Common:
    m = M()


common = Common()
common.m = 'shiyong'
del common.m
print(common.m)
print(type(common.m))
