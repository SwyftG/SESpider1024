# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Email1024Item(scrapy.Item):
    topic_id = scrapy.Field()
    topic_url = scrapy.Field()
    topic_title = scrapy.Field()
    topic_img_url = scrapy.Field()
    block_name = scrapy.Field()
    file_urls = scrapy.Field()
    file = scrapy.Field()