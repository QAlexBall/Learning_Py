# 单元测试
# TDD: Test-Driven Development(测试驱动开发)
# 单元测试是用来对一个模块, 一个函数或者一个类来进行正确性检验的测试工作
# 确保一个程序模块的行为副歌我们设计的测试用例
class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'!!!!!" % key)
	def __setattr__(self, key, value):
		self[key] = value
d = Dict(a=1, b=2)
d.a = 2
print(d, '\t', d['a'], '\t', d.a,)

import unittest
# 以test开头的方法就是测试方法, 不以test开头的方法不被认为是测试方法, 测试的时候不会被执行
class TestDict(unittest.TestCase):

# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法
# 这两个方法分别在每调用一个测试方法的前后被执行
# 例如在setUp()中连接数据库, 在tearDown()中关闭数据库, 这样就不必在每个测试方法中重复相同代码
	def setUp(self):
		print('SetUp...')
	def tearDown(self):
		print('tearDwon...', '\n')

	def test_init(self):
		d = Dict(a=2, b='test')
		self.assertEqual(d.a, 2)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))
		print('[In test_init]')

	def test_key(self):
	 	d = Dict()
	 	d['key'] = 'value'
	 	self.assertEqual(d.key, 'value')
	 	print('[In test_key]')

	def test_atrr(self):
	 	d = Dict()
	 	d.key = 'value'
	 	self.assertTrue('key' in d)
	 	self.assertEqual(d['key'], 'value')
	 	print('[In test_attr]')

	def test_keyerror(self):
	 	d = Dict()
	 	with self.assertRaises(KeyError):
	 		value = d['empty']
	 	print('[In test_keyerror]')

	def test_attrerror(self):
	 	d = Dict()
	 	with self.assertRaises(AttributeError):
	 		value = d.empty
	 	print('[In test_attrerror]')
if __name__ == '__main__':
	unittest.main()

