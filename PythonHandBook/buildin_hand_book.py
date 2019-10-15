from builtins import setattr, getattr


class MyClass:
    def __init__(self, name, name_id):
        self.name = name
        self.name_id = name_id

    def __repr__(self):
        if hasattr(self, 'id'):
            return 'name => [{}], name_id => [{}] id => [{}]'.format(self.name, self.name_id, self.id)
        return 'name => [{}], name_id => [{}]'.format(self.name, self.name_id)

    def __str__(self):
        if hasattr(self, 'id'):
            return 'name => [{}], name_id => [{}] id => [{}]'.format(self.name, self.name_id, self.id)
        return 'name => [{}], name_id => [{}]'.format(self.name, self.name_id)


mc = MyClass("chris", "1")
print(mc)
print(getattr(mc, 'name'))
print(hasattr(mc, 'name'))
print(hasattr(mc, 'id'))
print(setattr(mc, 'id', 'id_1'))
print(hasattr(mc, 'id'))
print(mc)
