import urllib
from scrapy.http import HtmlResponse



def getHtml(url):
	if url is None:
		return None
	request = urllib.request.Request(url)
	request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.360")
	response = urllib.request.urlopen(request)
	if response.getcode() != 200:
		return None
	return response.read()

def downloadPics(url):

    body = getHtml(url)
    html = HtmlResponse(url=url,body=body)
    pics = html.selector.xpath('//*[@class="gallary_item"]/div/div/table/tr/td/img/@src').extract()
    ahead = "http://www.xiumm.org"
    pics = [ahead + x for x in pics]
    return pics

def urlList(url):

    body = getHtml(url)
    html = HtmlResponse(url=url, body=body)
    urls = html.selector.xpath('//*[@class="gallary_wrap"]/div/div[1]/div[1]/table/tr/td/a/@href').extract()
    ahead = "http://www.xiumm.org"
    urls = [ahead + x for x in urls]
    return urls

if __name__ == '__main__':
    homeUrl = "http://www.xiumm.org/albums/page-2.html"
    urls = urlList(homeUrl)
    pics = []
    for url in urls:
        pics.extend(downloadPics(url))
    print(pics)
