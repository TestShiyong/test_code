def singleton(cls):
    instance_dict = {}

    def get_instance(*args, **kwargs):
        if cls not in instance_dict:
            instance_dict[cls] = cls(*args, **kwargs)
        return instance_dict[cls]

    return get_instance


@singleton
class Room:
    def __init__(self, name):
        self.name = name


@singleton
class Room2:
    def __init__(self, age):
        self.age = age


t1 = Room('shiyong')
t2 = Room()
print(id(t1))
print(id(t2))
print(t2.name)
t3 = Room2()
t4 = Room2()
print(id(t3))
print(id(t4))
