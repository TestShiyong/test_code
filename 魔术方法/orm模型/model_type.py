# 字段父类
class BaseFiled:
    pass


class IntFiled(BaseFiled):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError('value type must is int')

    def __delete__(self, instance):
        self.value = None


class StrFiled(BaseFiled):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            self.value = value
        else:
            raise TypeError('value type must is str')

    def __delete__(self, instance):
        self.value = None


class Boolean(BaseFiled):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            TypeError('value type must is bool')

    def __delete__(self, instance):
        self.value = None
