import scrapy
from project.items import ProjectItem

class ConterviewSpider(scrapy.Spider):
    name = 'conter'
    allowed_domains = ['https://www.youtube.com/']
    start_urls = ['https://www.youtube.com/watch?v=tkvJQ5x-eEY']

    def parse(self, response):
            name = response.xpath('//title//text()').extract_first('')
            views = response.xpath('//div[@class="view-count"]/text()').extract_first('')
            result = ProjectItem(name=name, views=views)
            yield result