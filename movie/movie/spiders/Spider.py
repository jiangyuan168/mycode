#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from movie.items import MovieItem
import re

class DoubanSpider(BaseSpider):
	name="douban"
	allowed_domains=["movie.douban.com"]
	start_urls=[]
	
	def start_requests(self):
		file_object = open('/home/zeus/movie_name.txt','r')
		try:
			url_head="http://movie.douban.com/subject_search?search_text="
			for line in file_object:
				self.start_urls.append(url_head+line)
			for url in self.start_urls:
				yield self.make_requests_from_url(url)
		finally:
			file_object.close()

	def parse(self,response):
		s=HtmlXpathSelector(response)
		movie_link=s.select('//*[@id="content"]/div/div[1]/div[2]/table[1]/tr/td[1]/a/@href').extract()
		if movie_link:
			yield Request(movie_link[0],callback=self.parse_item)

	def parse_item(self,response):
		s=HtmlXPathSelector(response)
		movie_name=s.selector('//*[@id="content"]/h1/span[1]/text()').extract()
		movie_director = s.select('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
		movie_writer = s.select('//*[@id="info"]/span[2]/span[2]/a/text()').extract()
		movie_description_paths = s.select('//*[@id="link-report"]')
		movie_description=[]
		for movie_description_path in movie_description_paths:
			ovie_description = movie_description_path.select('.//*[@property="v:summary"]/text()').extract()
		movie_roles_paths = s.select('//*[@id="info"]/span[3]/span[2]')
		movie_roles = []
		for movie_roles_path in movie_roles_paths:
			movie_roles = movie_roles_path.select('.//*[@rel="v:starring"]/text()').extract()
		movie_detail = s.select('//*[@id="info"]').extract()

		item=MovieItem()
		item['movie_name'] = ''.join(movie_name).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
		item['movie_director'] = movie_director[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_director) > 0 else ''
		item['movie_description'] = movie_description[0].strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';') if len(movie_description) > 0 else ''
		item['movie_writer'] = ';'.join(movie_writer).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
		item['movie_roles'] = ';'.join(movie_roles).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
		movie_detail_str = ''.join(movie_detail).strip()
		movie_language_str = ".*语言:</span> (.+?)<br><span.*".decode("utf8")
		movie_date_str = ".*上映日期:</span> <span property=\"v:initialReleaseDate\" content=\"(\S+?)\">(\S+?)</span>.*".decode("utf8")
		movie_long_str = ".*片长:</span> <span property=\"v:runtime\" content=\"(\d+).*".decode("utf8")
		pattern_language =re.compile(movie_language_str,re.S)
		pattern_date = re.compile(movie_date_str,re.S)
		pattern_date = re.compile(movie_date_str,re.S)
		movie_language = re.search(pattern_language,movie_detail_str)
		movie_date = re.search(pattern_date,movie_detail_str)
		movie_long = re.search(pattern_long,movie_detail_str)
		item['movie_language'] = ""
		if movie_language:
			item['movie_language'] = movie_language.group(1).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
		item['movie_date'] = ""
		if movie_date:
			item['movie_date'] = movie_date.group(1).strip().replace(',',';').replace('\'','\\\'').replace('\"','\\\"').replace(':',';')
		item['movie_long'] = ""
		if movie_long:
			item['movie_long'] = movie_long.group(1)
		yield item

