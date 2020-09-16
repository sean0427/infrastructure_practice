#!/usr/bin/python3

import uuid

class OrderModel():
    def __init__(self, base=None):
        self.base = base

    def getById(self, id):
        # query order data
        return dict(id = id)

    def create(self):
        return dict(id = str(uuid.uuid1()))
