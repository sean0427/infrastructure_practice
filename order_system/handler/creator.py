#!/usr/bin/python3

def getDataById(id):
    # TODO doing something create order

    return dict(
            id = id
            )

def lambda_handler(event, context):
    id = event['id']

    return getDataById(id)

