# coding=utf-8
import urllib.request

url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id13'
response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')
with open('./example.html', 'w') as f:
    f.write(text)
