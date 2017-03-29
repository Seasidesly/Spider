#coding = utf-8
from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import urllib.parse




#下载
class HtmlDownload(object):
	"""docstring for Html_downloader"""
	def download(self, url):
		if url is None:
			return None
		request = urllib.request.Request(url)
		request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.360")
		response = urllib.request.urlopen(request)
		if response.getcode() != 200:
			return None
		print("ok")
		return response.read()