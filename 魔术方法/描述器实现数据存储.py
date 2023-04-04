class CharFiled:

    def __init__(self, max_length=10):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) > self.max_length:
                raise ValueError('value length must less than {} '.format(self.max_length))
            else:
                self.value = value
        else:
            raise TypeError('value type must is str ')

    def __delete__(self, instance):
        self.value = None


class IntFiled:

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError('value type must is int ')

    def __delete__(self, instance):
        self.value = None


class Model(object):
    user = CharFiled(max_length=20)
    pwd = CharFiled(max_length=10)
    age = IntFiled()

model = Model()
model.user = 'shiyong'
model.pwd = 'password'
model.age = 18
print(model.user)
print(model.pwd)
print(model.age)
print(type(model.age))
