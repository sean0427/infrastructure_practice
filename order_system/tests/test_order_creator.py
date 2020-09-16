#!/usr/bin/python3

import pytest

from handler import creator

TEST_REQUEST = dict(
        id = 'test'
        )

TEST_ID_1 = 'test_id_1'
# first solution, not using unittest.mock
@pytest.fixture()
def model():
    class mock_model():
        def create(self):
            return dict(id=TEST_ID_1)
    return mock_model()

def test_create(model):
    creator.model = model
    response = creator.lambda_handler(TEST_REQUEST, None)

    assert response['id'] == TEST_ID_1
