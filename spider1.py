#coding utf-8
import urllib2
import urllib
import re
import time
from random import choice
iplist=['1.9.189.65:3128','27.24.158.130.80','27.24.158.154:80']
keywords=["NBA","CBA"]
for item in keywords:
	ip=choice(iplist)
	word=urllib.quote(item)
	url="https://sug.so.360.cn/suggest?callback=suggest_so&encodein=utf-8&encodeout=utf-8&format=json&fields=word,obdata&word="+word
	headers={
			"GET":url,
			"Host":"sug.so.360.cn",
			"Referer":"https://www.so.com/",
			"User_Agent":" Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0"
		}
	proxy_support=urllib2.ProxyHandler({'http':'http://'+ip})
	opener=urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
	req=urllib2.Request(url)
	for key in headers:
		req.add_header(key,headers[key])
	html=urllib2.urlopen(req).read()
	result=re.findall("\"(.*?)\"",html)
	r=('query','word','version','result','3.2.1','rec')
	for item in result:
		if item not in r:
			print item
	time.sleep(3)
