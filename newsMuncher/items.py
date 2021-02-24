# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class newsItem(Item):
    title = Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=Join())
    url = Field(output_processor=Join())
    author = Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=TakeFirst())
    date = Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=Join())
    article = Field(input_processor=MapCompose(remove_tags, str.strip), output_processor=Join())
    site = Field()
