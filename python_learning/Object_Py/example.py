std1 = { 'name' : 'Alex', 'score' : 99 }
std2 = { 'name' : 'Michael', 'score' : 59 }
def print_score(std):
	print('%s: %s' % (std['name'], std['score']))
print_score(std1)
print_score(std2)
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))
		

bart = Student('Bart Simpson', 58)
lisa = Student('Lisa Simpson', 78)
bart.print_score()
lisa.print_score()