# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LoadphotosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #movie_id=scrapy.Field()
    movie_size=scrapy.Field()
    movie_link=scrapy.Field()
    pass
