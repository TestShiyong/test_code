class Call:
    def __init__(self, func):
        self.fun = func

    def __call__(self, *args, **kwargs):
        print('这是类装饰器里面的功能，饭前洗洗手')
        self.fun()


@Call
def eat():
    print('开始吃饭')


eat()
