# -*- coding: utf-8 -*-

# Scrapy settings for loadphotos project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'loadphotos'

SPIDER_MODULES = ['loadphotos.spiders']
NEWSPIDER_MODULE = 'loadphotos.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'loadphotos (+http://www.yourdomain.com)'
USER_AGENT ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'
ITEM_PIPELINES = {
    'loadphotos.pipelines.LoadphotosPipeline':300,
}
DOWNLOAD_DELAY = 2
COOKIES_ENABLED=False
