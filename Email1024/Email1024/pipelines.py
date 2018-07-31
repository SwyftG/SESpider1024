# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
from .emailUtil import EmailHelper


class Email1024Pipeline(object):
    def process_item(self, item, spider):
        return item


class Email1024FilePipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for index, image_url in enumerate(item['file_urls']):
            # print("index: " + str(index) + " // " + image_url)
            if 'gif' in image_url:
                continue
            yield Request(image_url, meta={'name': item['topic_title'], 'index': str(index), 'block_name': item['block_name']})

    def file_path(self, request, response=None, info=None):
        # 因为'/'字符会在路径中转换成文件夹，所以要替换掉
        name = request.meta['name'].strip().replace('/', '-')
        if request.meta['index'] == '0':
            return request.meta['block_name'] + "/" + name + "/" + name + ".torrent"
        else:
            return request.meta['block_name'] + "/" + name + "/" + name + "-" + request.meta['index'] + ".jpg"

    def item_completed(self, results, item, info):
        emailHelper = EmailHelper()
        emailHelper.sendEmailWithAttr(results, item)
        return item