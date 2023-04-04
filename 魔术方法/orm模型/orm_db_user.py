from model_type import IntFiled, StrFiled, Boolean, BaseFiled


class FileMeatClass(type):
    def __new__(cls, name, base, dic, *args, **kwargs):
        t_name = name.lower()  # 将类名转化为小写，对应表的名称
        fields = {}  # 定义 模型字段 属性容器
        for k, v in list(dic.items()):
            # 如果模型字段 属性值是否为字段类型,把字段类型属性存储起来
            if isinstance(v, BaseFiled):
                fields[k] = v

        dic['t_name'] = t_name  # 表名存储
        dic['fields'] = fields # 字段属性存储
        return super().__new__(cls, name, base, dic)


# 所有模型类 父类
class BaseModel(metaclass=FileMeatClass):
    """
    所有模型类的父类
    1.实现指定元类
    2.模型类属性初始化

    """
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def save(self):
        dict_fields = {}
        t_name = self.t_name
        fields = self.fields
        for k in fields.keys():
            dict_fields[k] = getattr(self,k)

        print(dict_fields)


# 利用元类 实现模型类
class User(BaseModel):
    """
    用户模型类
    """
    user_name = StrFiled()
    pwd = StrFiled()
    age = IntFiled()
    live = Boolean()
    pass


xiaoming = User(user_name='xiaoming', pwd='lb123456', age=18, live=True)
print(xiaoming.age)
xiaoming.save()
