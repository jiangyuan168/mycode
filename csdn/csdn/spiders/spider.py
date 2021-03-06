#-*- coding:utf-8 -*-

from scrapy.spider import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from csdn.items import CsdnItem

class csdnSpider(Spider):
	name="csdn"
	download_delay=1
	allowed_domains=["blog.csdn.net"]
	start_urls=[
		"http://blog.csdn.net/u012286517/article/details/49556723"
	]

	def parse(self,response):
		sel=Selector(response)
		item=CsdnItem()
		title=sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()
		article_url = str(response.url)
		time=sel.xpath('//div[@id="article_details"]/div[2]/div/span[@class="link_postdate"]/text()').extract()
		readtimes=sel.xpath('//div[@id="article_details"]/div[2]/div/span[@class="link_view"]/text()').extract()
		item['title']=[n.encode('utf-8').replace("\r\n","").strip() for n in title]
		item['time']=[n.encode('utf-8') for n in time]
		item['readtimes']=[n.encode('utf-8') for n in readtimes]
		yield item
		#get next url	
		urls=sel.xpath('//li[@class="next_article"]/a/@href').extract()
		for url in urls:
			print url
			url="http://blog.csdn.net"+url
			print url
			yield Request(url,callback=self.parse)

		
