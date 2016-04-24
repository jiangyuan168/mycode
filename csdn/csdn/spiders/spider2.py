#-*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule  
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor  
from scrapy.selector import Selector 
from csdn.items import CsdnItem

class csdnSpider2(CrawlSpider):
	name="csdn2"
	download_delay=1
	allowed_domains=["blog.csdn.net"]
	start_urls=[
		"http://blog.csdn.net/u012286517/article/details/49556723"
	]
	rules = [  
        Rule(SgmlLinkExtractor(allow=('/u012286517/article/details'),  
                              restrict_xpaths=('//li[@class="next_article"]')),  
             callback='parse_item',  
             follow=True)  
    ]  
	def parse_item(self, response):
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

		
