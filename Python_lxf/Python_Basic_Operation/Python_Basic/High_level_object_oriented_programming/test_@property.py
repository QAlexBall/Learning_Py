
# 
import time as t 
print(t.time())
lt = t.localtime(t.time())
print(lt)
print(lt.tm_year)
print(t.struct_time.tm_year)
class Student(object):

	def __init__(self, name, score = 0):
		self.name = name
		self._score = score
	@property # 把一个getter方法变成属性
	def score(self):
		return self._score

	@score.setter # 负责把一个setter方法变成属性赋值
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		print(self.name, 'score is: ', end='')
		self._score = value
	@property
	def birth(self):
		return self._brith
	@birth.setter
	def birth(self, value):
		self._birth = value
	@property
	def age(self):
		print(self.name, 'age is: ', end='')
		return lt.tm_year - self._birth
s1 = Student('s1')
s1.birth = 1997
print(s1.age)
s = Student('s')
s.score = 90 # 实际上转化成s.set_score(90)
print(s.score) # 实际上转化成s.get_score()

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
c = Celsius()
c.temperature = 10
print(c.temperature)


'''	
class Student(object):

	def get_score(self):
		return self._score
	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = value

s = Student()
s.set_score(25)
print(s.get_score())
s.set_score(999)		# Output: AttributeError: 'Student' object has no attribute 'score'
'''