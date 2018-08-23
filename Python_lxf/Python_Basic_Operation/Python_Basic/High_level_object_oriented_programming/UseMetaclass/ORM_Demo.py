# ORM(Object Relational Mapping), 对象-关系映射, 就是把关系数据库的一行
# 映射为一个对象, 也就是一个类对应一个表要编写一个ORM框架, 
# 所有的类智能动态定义, 因为只有使用者才能根据表的结构定义出相应的类

# 接口实现ORM :
# 首先定义Field类, 它负责保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


# 在Field基础上, 进一步定义各种类型的Field
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


# 编写ModelMetaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


# 基类Model
class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'Insert into %s (%s) values (%s)' % \
              (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))


# 编写底层模块第一步, 先写调用接口
# 比如, 使用者如果使用这个ORM框架, 想定义一个User类来操作对应数据库表User
class User(Model):
    # 定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


# 创建一个实例
u = User(id=123, name='Alex', email='Alex@email.com', password='my_passwd')
# 保存到数据库
u.save()
# 其中, 父类Model和属性类型StringField, IntegerField是由ORM框架提供的
# 剩下的魔术方法, 比如save()全部由metaclass自动完成, metaclass的编写会比较
# 复杂, 但是ORM的使用者用起来异常简单
