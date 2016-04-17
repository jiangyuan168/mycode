# -*- coding: utf-8 -*-

# Scrapy settings for movie project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'movie'

SPIDER_MODULES = ['movie.spiders']
NEWSPIDER_MODULE = 'movie.spiders'

# Disable cookies (enabled by default)
COOKIES_ENABLED=False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'movie (+http://www.movie.douban.com)'
DOWNLOAD_DELAY = 2
#RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'
ITEM_PIPELINES = {
    'movie.pipelines.MoviePipeline': 300,
}
LOG_LEVEL='INFO'
