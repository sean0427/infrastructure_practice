import pytest

from unittest.mock import Mock 
from mongomock import MongoClient

from handler.model.order_model import OrderModel

TEST_ID = 'TEST_ID'

@pytest.fixture()
def collection():
    return MongoClient().db.collection

@pytest.fixture()
def model(collection):
    return OrderModel(collection)

def test_somke_mock(model):
    assert model != None

def test_get_order_by_id(model, collection):
    id = collection.insert_one(dict(aa='aa')).inserted_id

    assert model.getById(id)['_id'] == id

def test_create_order(model, collection):
    id = model.create()

    obj = collection.find_one({'_id': id})

    assert obj != None
    assert obj['_id'] == id

