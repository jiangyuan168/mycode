#-*- coding:utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from loadphotos.items import LoadphotosItem
import urllib

class loadphotos(BaseSpider):
	name="photo"
	allowed_domains=["douban.com"]
	start_urls=[]
	f=open('photo.txt','w')
	for i in range(0,80,40):
		start_urls.append('https://movie.douban.com/celebrity/1040543/photos/?type=C&start=%d&sortby=vote&size=a&subtype=a'%i)
	
	global counter
	#uesed to named picture
	counter=0

	def parse(self,response):
		hxs=HtmlXPathSelector(response)
		pictures=hxs.select('//ul/li/div/a/img/@src').extract()
		sizes=hxs.select('//ul/li/div[@class="prop"]/text()').extract()
		items=[]
		item = LoadphotosItem()
		self.f=open('photo.txt','a')
		global counter
		for picture in pictures:		
			picture=picture.replace("thumb","photo")
			self.f.write(picture)
			self.f.write('\r\n')
			#item = LoadphotosItem()
			item['movie_link']=picture
			#loadphotos
			if picture:
				urllib.urlretrieve(picture,'pic//'+str(counter)+'.jpg')
				print counter
			items.append(item)
			counter=counter+1
		self.f.close()
		
		for size in sizes:
			item['movie_size']=size.replace('\n','').strip()
			items.append(item)
		
		return items



