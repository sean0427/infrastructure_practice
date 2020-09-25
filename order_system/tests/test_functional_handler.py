#!/usr/bin/python3

import random
import string
import pytest 

from handler import creator, getter

@pytest.fixture()
def request_id():
    id = random.sample(string.ascii_letters + string.digits, 8)

    return dict(id = id)

def test_create(request_id):
    pass

def test_get(request_id):
    getter.lambda_handler(request_id, None) 
