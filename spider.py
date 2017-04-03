
from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import urllib.parse
import sys

import HtmlParser
import URLManager
import HtmlDownload

class SpiderMain(object):
	def __init__(self):
		self.urls = URLManager.UrlManager()
		self.downloader = HtmlDownload.HtmlDownload()
		self.parser = HtmlParser.HtmlParser()

	def craw_two(self, root_url):
		count = 1
		opener = urllib.request.build_opener()
		opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36")]
		urllib.request.install_opener(opener)
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print("craw %d : %s" % (count, new_url))
				html_cont = self.downloader.download(new_url)
				new_urls, new_data_urls = self.parser.paser(new_url, html_cont)
				self.urls.add_new_urls(new_urls)
				print(len(new_data_urls))

				for new_data_url in new_data_urls:
					urllib.request.urlretrieve(new_data_url, "G:\\spider\\imagess\\" + str(count) + ".jpg")
					count += 1
					print("Done")

			except Exception as e:
				print("failed:" + str(e))

		print("Beautiful Done!!!")


	def craw_one(self, root_url):
		count = 1
		opener = urllib.request.build_opener()
		opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36")]
		urllib.request.install_opener(opener)

		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()
				print("craw %d : %s" %(count, new_url))
				html_cont = self.downloader.download(new_url)
				#print(html_cont)
				new_data_urls = self.parser.paser_one(new_url, html_cont)
				print("2")
				print(len(new_data_urls))

				for new_data_url in new_data_urls:
					urllib.request.urlretrieve(new_data_url, "G:\\spider2\\images\\" + str(count) + ".jpg")
					count += 1

			except Exception as e:
				print("failed:" + str(e))

		print("Beautiful Done!!!")

if __name__ == '__main__':
 	root_url = "http://www.xiumm.org/albums/imiss.html"
 	my_spider = SpiderMain()
 	my_spider.craw_one(root_url)
