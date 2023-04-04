class A:
    pass


class B(A):
    pass


a=A()
print(A.__dict__)
print(B.__dict__)
print(a.__dict__)