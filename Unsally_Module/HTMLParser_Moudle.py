# 编写一个搜索引擎, 第一个步使用爬虫爬取目标页面
# 第二步解析该HTML页面, 如何解析?
# HTML本质是XML的子集, 但是HTIML的语法没有XML那么严格
# 不能使用标准的DOM或SAX来解析HTML

# Python提供了HTMLParser来解析HTML

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print('handle_data', data)

	def handle_comment(self, data):
		print('handle_comment', '<!--', data, '-->')

	def handle_entityref(self, name):
		print('handle_entityref &#%s;' % name)

	def handle_charref(self, name):
		print('handle_charref &#%s;' % name)

parser = MyHTMLParser()
parser_feed = parser.feed('''<html>
	<head></head>
	<body>
	<!-- test html parser -->
		<p>Some <a href=\"#\">html</a> HTML&nbsp; tutorial...<br>END</p>
		</body></html>''')
print(parser)
# feed方法可以多次调用, 不一定以西放入整个HTML字符串
# 特殊字符有两种, 一种是英文表示&nbsp; 一种是数字表示&#1234, 都可以通过Parser解析出来
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print("a start tag:", tag, self.getpos())
parser = MyHTMLParser()
parser.feed('<div><p>"hello"</p></div>') 

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag, attrs):
    print('begin tag', tag)
  def handle_startendtag(self, tag, attrs):
    print('begin end tag', tag)
str1 = '<br>'
str2 = '<br/>'
parser = MyHTMLParser()

parser.feed(str1)    # 输出 "begin tag br"
parser.feed(str2)    # 输出 "begin end br"