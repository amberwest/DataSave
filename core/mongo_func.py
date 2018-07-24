# -*- coding:utf-8 -*-
# Time: 2018/6/14 14:43
from pymongo import MongoClient
from DataSave import config

class MongoFunc(object):
    def __init__(self):
        self.user = config.get('db_user')
        self.pwd = config.get('db_password')
        self.port = int(config.get('db_port'))
        self.host = config.get('db_host')
        self.database = config.get('db_database')
        self.table = config.get('db_table')

        self.client = MongoClient(host=self.host, port=self.port, connect=False)
        self.db = self.client[self.database]
        self.db.authenticate(name=self.user, password=self.pwd)
        self.collection = self.db[self.table]

    def insert(self, data):
        # update()、insert()方法和save()方法都将要弃用了，所以用update_one(filter, update, upsert)
        # 这里是如果data跟表里一样就直接更新
        self.collection.update_one(data, {"$set": data}, upsert=True)
