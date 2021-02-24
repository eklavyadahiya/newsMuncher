#https://blog.dipasquale.fr/en/2018/12/17/incremental-scraping-with-scrapy-and-mongo/
#in case the tutorial is needed again

import pymongo


class MongoProvider(object):

    collection_name = 'news'

    def __init__(self, uri, database):
        self.mongo_uri = uri
        self.mongo_db = database or 'news'

    def get_collection(self):
        self.client = pymongo.MongoClient(self.mongo_uri)
        return self.client[self.mongo_db][self.collection_name]

    def close_connection(self):
        self.client.close()
