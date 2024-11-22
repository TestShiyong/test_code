def two():
    a=100
    print('运行第二个函数')
    def theree(data):
        print(a)
        print('运行第三个个函数','传参：{}'.format(data))
    return theree

three=two()
three(1000)
print(three.__closure__)
#
