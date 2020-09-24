#!/usr/bin/python3

from pymongo import MongoClient

def getClient(url='127.0.0.1', port=27965):
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


