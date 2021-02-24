import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newsMuncher.items import newsItem
from scrapy.loader import ItemLoader
from newsMuncher.mongo_provider import MongoProvider

#scraper block start
class TheGuardianSpider(CrawlSpider):
    name = 'theguardian'
    allowed_domains = ['theguardian.com', 'www.theguardian.com']
    start_urls = ['https://www.theguardian.com/international']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        loader = ItemLoader(newsItem(), response)
        loader.add_value('url', response.url)
        loader.add_css('title', 'h1')
        loader.add_css('author', 'address a')
        loader.add_css('article', '.article-body-viewer-selector')
        loader.add_css('date', '.css-hn0k3p')
        loader.add_value('site', 'theguardian.com')
        return loader.load_item()
#scraper block end
