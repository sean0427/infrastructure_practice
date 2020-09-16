#!/usr/bin/python3

from .model.order_model import OrderModel

model = OrderModel()

def lambda_handler(event, context):
    return model.create()
