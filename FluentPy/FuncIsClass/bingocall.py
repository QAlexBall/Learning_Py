import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        for l in self._items:
            print(l)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick empty BingoCage.')
    
    def __call__(self):
        return self.pick()

bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())
print(callable(bingo))