#-*- coding: utf-8 -*-
import urllib2
import re

baidu_pan_user_agent = 'JUC(Linux;U;2.2;Zh_cn;HTC Desire;480*800;)UCWEB7.7.0.85/139/999'
baidu_pan_regex = r'href=\"(http\:\/\/d\.pcs\.baidu\.com\S*)\"\sid='

def get_baidu_pan_url(shareid, uk):
    url = 'http://pan.baidu.com/share/link?shareid=' + shareid + '&uk=' + uk
    baidu_request = urllib2.Request(url)
    baidu_request.add_header('User-Agent', baidu_pan_user_agent)
    data = urllib2.urlopen(baidu_request).read()
    regex = re.compile(baidu_pan_regex)
    match = re.search(regex, data)
    if match:
        real_url = match.group(1).replace('amp;', '')
        if real_url.startswith('http'):
            return real_url
    return None

def test():
    url = get_baidu_pan_url('430100', '2987247908')
    print(url)

if __name__ == '__main__':
    test()
