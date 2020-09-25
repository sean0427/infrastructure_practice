#!/usr/bin/python3

import os

from pymongo import MongoClient

def getClient(url=os.getenv('MONGO_DB'), port=os.getenv('MONGO_PORT')):
    print("mongo server info %s %s" % (url, port))

    return MongoClient(url, port)

class OrderModel():
    def __init__(self, collection=getClient()['db']['order']):
        self.collection = collection

    def getById(self, id):
        # query order data
        obj = self.collection.find_one({"_id": id})

        return obj

    def create(self):
        return self.collection.insert_one(dict()).inserted_id

