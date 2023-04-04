"""

对象唯一 任何时候创建对象都是第一个对象
"""


class Room:
    only_object = None

    def __new__(cls, *args, **kwargs):
        if not cls.only_object:
            cls.only_object = object.__new__(cls)
            return cls.only_object
        else:
            return cls.only_object


t1 = Room()
t1.name = 'shiyong'
t2 = Room()
print(t1.name)
print(t2.name)
