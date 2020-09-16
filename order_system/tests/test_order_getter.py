#!/usr/bin/python3

import pytest
from unittest.mock import MagicMock

from handler import getter
from handler.model.order_model import OrderModel

TEST_REQUEST = dict(
        id = 'test'
        )
TEST_ID_1 = 'test_id_1'

@pytest.fixture(scope="module")
def model():
    model = OrderModel()
    model.getById = MagicMock(return_value=dict(id=TEST_ID_1))

    return model

def test_get(model):
    getter.model = model
    response = getter.lambda_handler(TEST_REQUEST, None)

    assert response['id'] == TEST_ID_1
