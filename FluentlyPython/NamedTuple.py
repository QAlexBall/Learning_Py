from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.9330, (35.6897222, 139.691667))
print(tokyo)
