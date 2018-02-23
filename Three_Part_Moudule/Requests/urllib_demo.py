# -*- coding: utf-8 -*-
import urllib.request
import urllib

URL_IP = 'https://www.baidu.com/ip'

def use_simple_urllib():
	response = urllib.request.urlopen(URL_IP)
	print('>>>>>Response Header:')
	print(response.info())
	print('>>>>>Response Body:')
	print(''.join([line for line in response.readlines()]))

if __name__ == '__main__':
	print('>>>>>Use simple urllib')
	use_simple_urllib()

