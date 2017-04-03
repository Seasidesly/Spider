# coding = utf-8
import urllib.request
import urllib
import time
import ssl


class chinaUnicom(object):
    """docstring for chinaUnicom."""

    def getHtml(self, url):
        if url is None:
            return None
        request = urllib.request.Request(url)
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/36.0.1941.0 Safari/537.360")
        conText = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=conText)
        if response.getcode() == 200:
            print("ok")
        else:
            print("false")

if __name__ == '__main__':
    homeUrl = "https://ws.nciic.org.cn/nciic_ws/services/NciicServices?wsdl"
    url = "http://www.xiumm.org"
    my_ping = chinaUnicom()
    while 1:
        my_ping.getHtml(homeUrl)
        times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(times)
        time.sleep(60)
