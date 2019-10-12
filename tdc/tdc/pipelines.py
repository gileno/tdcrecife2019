# -*- coding: utf-8 -*-

import dataset
import datetime as dt


class TdcPipeline(object):

    def open_spider(self, spider):
        self.conn = dataset.connect('sqlite:///db.sqlite3')

    def process_item(self, item, spider):
        item['updated'] = dt.datetime.now()
        self.conn['items'].insert(item)
        return item
