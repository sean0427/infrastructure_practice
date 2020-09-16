import pytest

from handler.model.order_model import OrderModel

TEST_ID = 'TEST_ID'

@pytest.fixture()
def model():
    return OrderModel()

def test_order_model(model):
    assert model != None

def test_get_order_by_id(model):
    assert model.getById(TEST_ID)['id'] == TEST_ID

def test_create_order(model):
    assert model.create(TEST_ID)['id'] == TEST_ID
