#!/usr/bin/python3
import handler

TEST_DATA = dict(
        data = 'test'
        )

def test_echo():
    assert handler.lambda_handler(TEST_DATA, None) == 'test'
