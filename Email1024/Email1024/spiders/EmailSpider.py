# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from ..items import Email1024Item
from ..settings import SPIDER_NAME, ROOT_URL, BLOCK_INFO, MAX_PAGES,AUTHOR_NAME


class EmailspiderSpider(scrapy.Spider):
    name = SPIDER_NAME
    root_url = ROOT_URL
    max_pages = MAX_PAGES

    def start_requests(self):
        for key in BLOCK_INFO:
            request_url = self.root_url + "thread0806.php?fid=" + str(key) + "&search=&page=1"
            yield Request(url=request_url, callback=self.parse_block_page, meta={'block_name': BLOCK_INFO[key]})


    def parse_block_page(self, response):
        content = response.body
        response_url_list = response.url.split('/')
        page_num = response_url_list[-1].split('=')[-1]
        soup = BeautifulSoup(content, "html.parser")
        block_name = response.meta['block_name']
        temp_list = soup.find_all('a', attrs={'href': True, 'id': True})
        for item in temp_list:
            if "htm" not in item['href']:
                continue
            topic_id = item['href'].split('/')[3].split('.')[0]
            if len(topic_id) < 6:
                continue
            topic_url = self.root_url + item['href']
            yield Request(url=topic_url, callback=self.parse_poster_page,
                          meta={'topic_id': topic_id, 'block_name': block_name})
        if int(page_num) < self.max_pages:
            cur_url = response.url
            num = 0 - len(page_num)
            next_url = cur_url[:num] + str(int(page_num) + 1)
            yield Request(url=next_url, callback=self.parse_block_page, meta={'block_name': block_name}, dont_filter=True)

    def parse_poster_page(self, response):
        content = response.body
        soup = BeautifulSoup(content, "html.parser")
        title_list = soup.find_all('h4')
        topic_title = title_list[0].text
        topic_id = response.meta['topic_id']
        block_name = response.meta['block_name']
        topic_url = response.url
        print(topic_title)
        img_list = soup.find_all('img')
        topic_img_list = list()
        image_count = 0
        for item in img_list:
            if "src" not in item.attrs and "data-src" not in item.attrs:
                continue
            if "src" in item.attrs:
                if 'gif' in item['src']:
                    continue
            elif "data-src" in item.attrs:
                if 'gif' in item['data-src']:
                    continue
            if image_count < 4:
                if 'src' in item.attrs:
                    topic_img_list.append(item['src'])
                elif 'data-src' in item.attrs:
                    topic_img_list.append(item['data-src'])
                image_count = image_count + 1
            else:
                break
        b_list= soup.find_all('th')
        a_list = soup.find_all('a')
        author_name=''
        for item in b_list :
            for key in AUTHOR_NAME:
                if key not in item.text :
                    continue
                else :
                    author_name=key
        if len(author_name) == 0:
            return
        topic_torrent_url = ""
        for item in a_list:
            if "rmdown" in item.text:
                topic_torrent_url = item.text
        if topic_torrent_url != "":
            yield Request(url=topic_torrent_url, callback=self.parse_torrent_page,
                          meta={'topic_title': topic_title,
                                'topic_img_list': topic_img_list,
                                'topic_url': topic_url,
                                'topic_id': topic_id,
                                'block_name': block_name,
                                'author_name': author_name})

    def parse_torrent_page(self, response):
        content = response.body
        topic_title = response.meta['topic_title']
        soup = BeautifulSoup(content, "html.parser")
        topic_id = response.meta['topic_id']
        topic_url = response.meta['topic_url']
        topic_img_url = response.meta['topic_img_list']
        block_name = response.meta['block_name']
        topic_torrent_url = response.url
        author_name=response.meta['author_name']
        reff_value = soup.findAll(attrs={'name': 'reff'})
        ref_value = soup.findAll(attrs={'name': 'ref'})
        torrent_download_url = topic_torrent_url.split('?')[0].replace('link', 'download') + "?reff=" + reff_value[0][
            'value'] + "&ref=" + ref_value[0]['value']

        fileItem = Email1024Item()
        fileItem['topic_title'] = topic_title
        fileItem['topic_id'] = topic_id
        fileItem['topic_url'] = topic_url
        fileItem['block_name'] = block_name
        fileItem['topic_img_url'] = topic_img_url
        fileItem['author_name']= author_name
        urlList = [torrent_download_url]
        for img_url in topic_img_url:
            urlList.append(img_url)
        fileItem['file_urls'] = urlList
        return fileItem
