from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging
from newsMuncher.mongo_provider import MongoProvider

log = logging.getLogger()
settings = get_project_settings()

class MongoPipeline(object):

    def __init__(self, settings):
        self.mongo_provider = MongoProvider(
            settings.get('MONGO_URI'),
            settings.get('MONGO_DATABASE')
        )

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        self.collection = self.mongo_provider.get_collection()

    def close_spider(self, spider):
        self.mongo_provider.close_connection()

    def process_item(self, item, spider):
        required_fields = ['article']
        if all(field in item for field in required_fields):
            self.collection.find_one_and_update(
                {"url": item["url"]},
                {"$set": dict(item)},
                upsert=True
            )
            return item
        else:
            raise DropItem("Not an article")



# class MongoPipeline(object):
#     collection_name = settings.get('MONGO_COLLECTION')
#
#     def __init__(self, mongo_uri, mongo_db):
#         self.mongo_uri = mongo_uri
#         self.mongo_db = mongo_db
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_uri=settings.get('MONGO_URI'),
#             mongo_db=settings.get('MONGO_DATABASE')
#         )
#
#     def open_spider(self, spider):
#         self.client = pymongo.MongoClient(self.mongo_uri)
#         self.db = self.client[self.mongo_db]
#
#     def close_spider(self, spider):
#         self.client.close()
#
#     def process_item(self, item, spider):
#         self.db[self.collection_name].find_one_and_update(
#             {"url": item["url"]},
#             {"$set": dict(item)},
#             upsert=True
#         )
#         return item




class NewsmuncherPipeline:
    def process_item(self, item, spider):
        return item
