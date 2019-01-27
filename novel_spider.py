# -*- coding:UTF-8 -*-
#获取小硕正文
import requests
import html2text
from bs4 import BeautifulSoup
import scrapy
from scrapy.selector import Selector
import sys

h = html2text.HTML2Text()
h.ignore_links = False
h.ignore_images = True


if __name__ == '__main__':
	server = 'http://www.biqukan.com/'
	target_index = 'http://www.biqukan.com/1_1094'
	req = requests.get(url=target_index)
	index_list = target = Selector(text=req.text).xpath('//div[@class="listmain"]//dd/a/@href').extract()
	print(index_list)
	
	# target = 'http://www.biqukan.com/1_1094/5403177.html'
	# req = requests.get(url=target)
	# html = req.text
	# bf = BeautifulSoup(html)
	# texts = bf.find_all('div', class_='showtxt')
	# print(texts[0].text.replace('\xa0' * 8, '\n'))
	
	'''
	find_all匹配的返回的结果是一个列表。提取匹配结果后，使用text属性，提取文本内容，滤除br标签。
	随后使用replace方法，剔除空格，替换为回车进行分段。
	&nbsp;在html中是用来表示空格的。replace('\xa0'*8,'\n\n')就是去掉下图的八个空格符号，并用回车代替
	'''
	
	# content_html = Selector(text=req.text).xpath('//div[@class="showtxt"][1]').extract()
	# print(content_html)
	# content = h.handle(content_html[0])
	# print(content)
	#