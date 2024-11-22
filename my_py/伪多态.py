class Base:
    def func(self):
        print('动物类型 会走路')


class Dog(Base):
    def func(self):
        print(' 这个是狗 可以跑步')


class Cat(Base):
    def func(self):
        print(' 这个是猫 可以走猫步')


class Pig(Base):
    def func(self):
        print('动物类型 慢慢走路')

class Ya(Base):
    pass



a = Dog()
b = Cat()
c = Pig()
d = Ya()
a.func()
b.func()
c.func()
d.func()

