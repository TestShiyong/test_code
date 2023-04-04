"""
___str__方法
___repr__方法


print（）,str(),format()会调用___str___方法,找不到___str___方法会调用 ___repr___方法，必须返回str类型值
"""


class T1:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('调用了 ___str___方法')
        return self.name

    def __repr__(self):
        print('调用了 ___repr方法___')
        return 'aaaaa'


new_t1 = T1('shiyong')
print(new_t1)
str(new_t1)
format(new_t1)
print(repr(new_t1))