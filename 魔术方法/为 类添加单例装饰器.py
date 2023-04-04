def only_object(cls):
    object_dict = {}

    def fun(*args, **kwargs):
        if cls in object_dict:
            return object_dict[cls]
        else:
            object_dict[cls] = cls(*args, **kwargs)
            return object_dict[cls]

    return fun


@only_object
class Room:
    def __init__(self, name):
        self.name = name


@only_object
class Room2:
    def __init__(self, age):
        self.age = age


t1 = Room('shiyong')
t2 = Room()
print(id(t1))
print(id(t2))
print(t2.name)
t3 = Room2(18)
t4 = Room2()
print(id(t3))
print(id(t4))
print(t4.age)