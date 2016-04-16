# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_name=scrapy.Field()
    movie_director=scrapy.Field()
    moviewriter=scrapy.Field()
    movie_roles=scrapy.Field()
    movie_language=scrapy.Field()
    movie_date=scrapy.Field()
    movie_long=scrapy.Field()
    movie_description=scrapy.Field()

