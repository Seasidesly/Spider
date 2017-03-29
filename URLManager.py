#coding = utf-8
from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import urllib.parse



#url管理
class UrlManager(object):
	def __init__(self):
		self.new_urls = set()
		self.old_urls = set()
		self.data_urls = set()

	def add_new_url(self, url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url = self.new_urls.pop()
		self.old_urls.add(new_url)
		return new_url

	def add_new_urls(self, urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)

	def add_new_data_urls(self, data_urls):
		if data_urls is None or len(data_urls) == 0:
			return
		for data_url in data_urls:
			if data_url is None:
				return
			self.data_urls.add(data_url)



