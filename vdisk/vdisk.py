#-*- coding: utf-8 -*-
import urllib2
import re

vdisk_user_agent = 'JUC(Linux;U;2.2;Zh_cn;HTC Desire;480*800;)UCWEB7.7.0.85/139/999'
vdisk_regex = r'\"uid\"\:\"(\d+)\"\,\"copy_ref\"\:\"\w+\"\,\"fid\"\:(\d+)\,\"name'

def get_vdisk_url(id):
    url = 'http://vdisk.weibo.com/wap/s/' + id
    vdisk_request = urllib2.Request(url)
    vdisk_request.add_header('User-Agent', vdisk_user_agent)
    data = urllib2.urlopen(vdisk_request).read()
    regex = re.compile(vdisk_regex)
    match = re.search(regex, data)
    if match:
        uid = match.group(1)
        fid = match.group(2)
        if (uid.isdigit() and fid.isdigit()):
            return 'http://openapi.vdisk.me/?m=file&a=jump_to_s3&uid=' + uid + '&fid=' + fid
    return None

def test():
    url = get_vdisk_url('yntEB')
    print(url)

if __name__ == '__main__':
    test()
