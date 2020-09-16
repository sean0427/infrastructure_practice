from handler import creator

TEST_REQUEST = dict(
        id = 'test'
        )

def test_create():
    response = creator.lambda_handler(TEST_REQUEST, None)

    assert response['id'] == TEST_REQUEST['id']
