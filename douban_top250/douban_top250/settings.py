# -*- coding: utf-8 -*-

# Scrapy settings for douban_top250 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douban_top250'

SPIDER_MODULES = ['douban_top250.spiders']
NEWSPIDER_MODULE = 'douban_top250.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_top250 (+http://www.yourdomain.com)'
ITEM_PIPELINES={
    'douban_top250.pipelines.DoubanTop250Pipeline':300,
}
LOG_LEVEL='DEBUG'

DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'
COOKIES_ENABLED = True
