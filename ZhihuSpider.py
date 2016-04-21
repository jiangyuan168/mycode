# -*- coding: utf-8 -*-
'''
网络爬虫之用户名密码及验证码登陆：爬取知乎网站
'''
import requests
import ConfigParser
from bs4 import BeautifulSoup
import re
import urllib
import urllib2

def create_session():
    cf = ConfigParser.ConfigParser()
    cf.read('config.ini')
    cookies = cf.items('cookies')
    cookies = dict(cookies)
    from pprint import pprint
    pprint(cookies)
    email = cf.get('info', 'email')
    password = cf.get('info', 'password')

    session = requests.session()
    login_data = {'email': email, 'password': password}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36',
        'Host': 'www.zhihu.com',
        'Referer': 'http://www.zhihu.com/'
    }
    r = session.post('http://www.zhihu.com/login/email', data=login_data, headers=header)
    if r.json()['r'] == 1:
        print 'Login Failed, reason is:',
        for m in r.json()['data']:
            print r.json()['data'][m]
        print 'So we use cookies to login in...'
        has_cookies = False
        for key in cookies:
            if key != '__name__' and cookies[key] != '':
                has_cookies = True
                break
        if has_cookies is False:
            raise ValueError('请填写config.ini文件中的cookies项.')
        else:
            r = session.get('http://www.zhihu.com/login/email', cookies=cookies) # 实现验证码登陆


    return session, cookies


if __name__ == '__main__':
    requests_session, requests_cookies = create_session()
    url = 'http://www.zhihu.com'
    reqs= requests_session.get(url, cookies=requests_cookies) # 已登陆
    content=reqs.content
    with open('url.html', 'w') as fp:
        fp.write(content)
    soup=BeautifulSoup(content)
    user_name=soup.find("div",class_="top-nav-profile").a.span.string
    print "user_name:%s" % (user_name)
    pic_url=soup.find("div",class_="top-nav-profile").a.img
    urllib.urlretrieve(pic_url['src'],'/home/zeus/pic1/'+'1.jpg')
    print "potos:%s" %(pic_url['src'])
    #a=soup.find("div",id="js-home-feed-list").div
    #b=a.find("div",class_="content").h2.a.get_text()
    #print b
    for topic in soup.find_all("div",class_="feed-main",limit=10):
	#print top
	print '-------------------------------------------------------'
	topic_source=topic.find("div",class_="feed-source").a.get_text()
	print "topic source:%s" %(topic_source)
	question=topic.find("div",class_="content").a.get_text()
	print "question:%s" %(question)
	votecount=topic.find("div",class_="zm-item-vote").a.get_text()
	print "votecount:%s" %(votecount)
	answer=topic.find("div",class_="zm-item-rich-text js-collapse-body")
	if answer:
		print "answer_name:%s" %(answer['data-author-name'])
	print '-------------------------------------------------------'
    
    
