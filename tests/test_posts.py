import pytest
from data.post_payloads import VALID_POST_PAYLOAD

REQUIRED_FIELDS = ["userId", "id", "title", "body"]


def assert_status_code(response_raw, expected_code):
    assert response_raw.status_code == expected_code, f"expected '{expected_code}' does not match actual '{response_raw.status_code}'"

def assert_json_match_required_fields(response_body):
    for field in REQUIRED_FIELDS:
        assert field in response_body, f"{field} is missing in json"

def assert_json_fields_match_payload(response_body, payload, post_id=None):
    if post_id is not None:
        assert response_body["id"] == post_id, f"expected id '{post_id} does not match actual id '{response_body["id"]}'"
    for field, value in payload.items():
        assert response_body[field] == value, f"expected payload '{payload[field]}' does not match actual '{response_body[field]}'"

# get post
## positive tests
@pytest.mark.parametrize("post_id", range(1, 3))
def test_get_post_returns_200_and_json_match_required_fields(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert_status_code(response, 200)

    response_json = response.json()
    assert_json_match_required_fields(response_json)

## negative tests
@pytest.mark.parametrize("post_id", [-1, 0])
def test_get_post_returns_404_and_empty_json_for_invalid_id(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert_status_code(response, 404)

    response_json = response.json()
    assert response_json == {}, "json should be empty"

# create post
## positive tests
def test_create_post_returns_201_and_json_match_payload(posts_client):
    response = posts_client.create_post(VALID_POST_PAYLOAD)
    assert_status_code(response, 201)

    response_json = response.json()
    assert_json_match_required_fields(response_json)
    assert_json_fields_match_payload(response_json, VALID_POST_PAYLOAD)

# update post
## positive tests
@pytest.mark.parametrize("post_id", range(1, 3))
def test_update_post_returns_200_and_json_match_payload(posts_client, post_id):
    response = posts_client.update_post(post_id, VALID_POST_PAYLOAD)
    assert_status_code(response, 200)

    response_json = response.json()
    assert_json_match_required_fields(response_json)
    assert_json_fields_match_payload(response_json, VALID_POST_PAYLOAD, post_id)

# delete test
## positive tests
@pytest.mark.parametrize("post_id", range(1, 3))
def test_delete_post_returns_200_and_empty_json(posts_client, post_id):
    response = posts_client.delete_post(post_id)
    assert_status_code(response, 200)

    response_json = response.json()
    assert response_json == {}, "json should be empty"
