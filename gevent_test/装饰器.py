"""
无参装饰器





def check(fun):

    def login():
        username = 'shiyong'
        password = '123456'
        ac = input('input a account:')
        pwd = input('input a password:')
        if ac == username and pwd == password:
            print('登录成功')
            fun()
        else:
            print('密码  或 账号错误')

    return login


    @check #add_cat=login()
def add_cat():
    print('这是一个网站')


add_cat()




"""

"""
#带参装饰器



def add(func):


    def fun(a,b):
        print('计算 两个数相乘：a+b={}'.format(a+b))
        func(a,b)
    return fun



@add
def add_number(a,b):
    print('计算 两个数相加：a+b={}'.format(a+b))

add_number(5,9)
"""

"""
通用装饰器


def common_func(func):
    def fun(*args, **kwargs):
        print('这是扩展的功能')
        func(*args, **kwargs)

    return fun

@common_func
def goods_list(number):
    print('这是列表页第：{} 页'.format(number))

@common_func
def home_page():
    print('这是网站首页')

goods_list(9)
print('-------------这是两个函数的分割线----------------')
home_page()

"""

"""
类装饰器



"""






"""
多个装饰器




def common_func(func):
    def fun(*args, **kwargs):
        print("这个是 通用装饰器")
        return func(*args, **kwargs)

    return fun


def check(fun):
    def login():
        username = 'shiyong'
        password = '123456'
        ac = input('input a account:')
        pwd = input('input a password:')
        if ac == username and pwd == password:
            print('登录成功')
            fun()
        else:
            print('密码  或 账号错误')

    return login

@check
@common_func
def test():
    print('测试函数')


test()

"""




def common_func(func):
    def fun(*args, **kwargs):
        print('这是扩展的功能')
        return func(*args, **kwargs)

    return fun


@common_func
class Page:
    def __init__(self, name):
        self.name = name


new_page = Page('shiyong')
print(new_page)
print(new_page.name)