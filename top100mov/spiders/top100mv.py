import scrapy

from top100mov.items import Top100MovItem

class Top100mvSpider(scrapy.Spider):
    name = 'top100mv'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/v/popular/rank/movie']

    def parse(self, response):
        # print(response.status)
        # print(response.css('title::text').extract_first())
        mv_list = response.css('li.rank-item')
        for mv in mv_list:
            item = Top100MovItem()
            item['name'] = f'《{mv.css("a.title::text").extract_first()}》'
            item['time'] = mv.css('div.pgc-info::text').extract_first()
            item['score'] = mv.css('div.pts > div::text').extract_first()
            yield item