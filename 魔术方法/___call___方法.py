"""

如果有call方法是可被调用
"""


class Call:
    def __init__(self):
        print('运行了init方法')

    def __call__(self):
        print('调用了 类的call方法')


t1 = Call()
t1()
