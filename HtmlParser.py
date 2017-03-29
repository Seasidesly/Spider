#coding = utf-8
from bs4 import BeautifulSoup
import urllib.request
import urllib
import re
import urllib.parse


#过滤
class HtmlParser(object):
	def get_new_urls(self, page_url, soup):
		new_urls = set()
		url_first = "http://www.xiumm.org"
		#http://www.xiumm.org/photos/MiStar-16894.html
		links = soup.find_all("a", href = re.compile(r"/photos/"))
		for link in links:
			new_url = link["href"]
			new_full_url = urllib.parse.urljoin(url_first, new_url)
			print(new_full_url)
			new_urls.add(new_full_url)
		return new_urls

	def get_new_data_urls(self, page_url, soup):

		img_urls = set()
		url_first = "http://www.xiumm.org"
		img_nodes = soup.find_all("img", src = re.compile(r"/data/"))
		for img_node in img_nodes:
			img_url = img_node["src"]
			img_full_url = urllib.parse.urljoin(url_first, img_url)
			print(img_full_url)
			img_urls.add(img_full_url)

		return img_urls

	def get_new_data_urls_one(self, page_url, soup):

		img_urls = set()
		alts = set()

		img_nodes = soup.find_all("img", src = re.compile(r"/data/t/"))
		#print(img_nodes)
		for img_node in img_nodes:
			img_url = img_node["src"]
			print("url:" + img_url)
			img_urls.add(img_url)

			alt = img_node["alt"]
			print("alt" + alt)
			alts.add(alt)

		return img_urls


	def paser_one(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return
		print("ok")
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = "utf-8")
		print("yes")
		new_data_urls = self.get_new_data_urls_one(page_url, soup)
		return new_data_urls



	def paser(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return
		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = "utf-8")
		new_urls = self.get_new_urls(page_url, soup)
		new_data = self.get_new_data_urls(page_url, soup)
		return new_urls, new_data