#!/usr/bin/python3

from handler import getter

TEST_REQUEST = dict(
        id = 'test'
        )

def test_get():
    response = getter.lambda_handler(TEST_REQUEST, None)

    assert response['id'] == TEST_REQUEST['id']
