#!/usr/bin/python3

def getDataById(id):
    return dict(
            id = id
            )

def lambda_handler(event, context):
    id = event['id']

    # TODO find data

    return getDataById(id)
