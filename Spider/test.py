import urllib.request
response = urllib.request.urlopen("https://www.baidu.com")
print (response.readlines())

