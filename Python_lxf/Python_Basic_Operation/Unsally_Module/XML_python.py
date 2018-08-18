# DOM vs SAX
# 操作XML有两种方法: DOM和SAX. DOM会把整个XML读入内存, 
# 解析为树, 因此占用内存大解析慢, 优点是可以任意遍历树的节点
# SAX是流模式, 边读边解析, 占用内存小, 解析快, 缺点就是需要自己处理事件

# 正常情况下, 优先考虑SAX
# 在Python中SAX解析XML非常简介, 通常我们关心的事件是
# start_element, end_element和char_data


# example
# 当SAX解析器读到一个节点时:
# <a href="/">python</a>
# 会产生3个事件
# 1. start_element事件, 在读取<a href="/">时;
# 2. char_data事件, 在读取python时;
# 3. end_element事件, 在读取</a>时;
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

	def end_element(self, name):
		print('sax:end_element: %s' % name)

	def char_data(slef, text):
		print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
	<li><a href="/python">Python</a></li>
	<li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
ParserCharacterDataHandler = handler.char_data
parser.Parse(xml)

# 要读取一大段字符串时, CharacterDataHandler可能被多次调用,
# 所以需要自己保存起来, 在EndElementHandler里面再合并

# 生成XML, 最简单有效的生成XML的方法是拼接字符串

L = []
L.append(r'<?xml version="1"?>')
L.append(r'<root>')
L.append(('some & data'))
L.append(r'</root>')
print(''.join(L))