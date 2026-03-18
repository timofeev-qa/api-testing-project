import pytest
from client.posts_client import get_post, create_post, update_post, delete_post
from data.post_payloads import PAYLOAD_POST_VALID, PAYLOAD_POST_WITH_NULL_FIELDS, PAYLOAD_POST_WITH_WRONG_USERID_KEY, PAYLOAD_POST_WITHOUT_TITLE

REQUIRED_FIELDS = ["userId", "id", "title", "body"]


def payload_matches_response(response_data, payload, post_id):
    if post_id is not None:
        if post_id != response_data["id"]:
            return False
    for field, value in payload.items():
        if response_data[field] != value:
            return False
    return True

# positive tests
@pytest.mark.parametrize("post_id", range(1, 4))
def test_get_post_returns_200_and_fields_match_response_structure(base_url, post_id, headers):
    response = get_post(base_url, post_id, headers)
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in REQUIRED_FIELDS:
        assert field in response_json, f"{field} is missing in json"

def test_create_post_returns_201_and_fields_matches_payload(base_url, headers):
    response = create_post(base_url, headers, PAYLOAD_POST_VALID)
    assert response.status_code == 201

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in REQUIRED_FIELDS:
        assert field in response_json, f"{field} is missing in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_VALID, None), "response does not match payload"
    
@pytest.mark.parametrize("post_id", range(1, 4))
def test_update_post_returns_200_and_fields_matches_payload(base_url, post_id, headers):
    response = update_post(base_url, post_id, headers, PAYLOAD_POST_VALID)
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in REQUIRED_FIELDS:
        assert field in response_json, f"{field} is missing in json"
    
    assert payload_matches_response(response_json, PAYLOAD_POST_VALID, post_id), "response does not match payload"

@pytest.mark.parametrize("post_id", range(1, 4))
def test_delete_post_returns_200_and_empty_json(base_url, post_id, headers):
    response = delete_post(base_url, post_id, headers)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json == {}, "json should be empty"

## negative tests
@pytest.mark.parametrize("post_id", [-1, 0, 9_999_999_999])
def test_get_post_by_invalid_postid_returns_404_and_empty_json(base_url, post_id, headers):
    response = get_post(base_url, post_id, headers)
    assert response.status_code == 404

    response_json = response.json()
    assert response_json == {}, "json should be empty"

def test_create_post_returns_201_and_null_payload_fields(base_url, headers):
    response = create_post(base_url, headers, PAYLOAD_POST_WITH_NULL_FIELDS)
    assert response.status_code == 201

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in REQUIRED_FIELDS:
        assert field in response_json, f"{field} is missing in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITH_NULL_FIELDS, None), "response does not match payload"

def test_create_post_returns_201_with_wrong_payload_key(base_url, headers):
    response = create_post(base_url, headers, PAYLOAD_POST_WITH_WRONG_USERID_KEY)
    wrong_key = "userID"
    assert response.status_code == 201

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    assert wrong_key in response_json, "key userID is missing in json"
    assert "userId" not in response_json, "key userId should not be in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITH_WRONG_USERID_KEY, None), "response does not match payload"

def test_create_post_returns_201_without_required_key(base_url, headers):
    response = create_post(base_url, headers, PAYLOAD_POST_WITHOUT_TITLE)
    required_fields = REQUIRED_FIELDS.copy()
    required_fields.remove("title")
    assert response.status_code == 201

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in required_fields:
        assert field in response_json, f"{field} is missing in json"
    
    assert "title" not in response_json, "key title should not be in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITHOUT_TITLE, None), "response does not match payload"

@pytest.mark.parametrize("post_id", [-1, 0, 9_999_999_999])
def test_update_post_by_invalid_postid_returns_500(base_url, post_id, headers):
    response = update_post(base_url, post_id, headers, PAYLOAD_POST_VALID)
    assert response.status_code == 500

@pytest.mark.parametrize("post_id", range(1, 4))
def test_update_post_returns_200_and_null_payload_fields(base_url, post_id, headers):
    response = update_post(base_url, post_id, headers, PAYLOAD_POST_WITH_NULL_FIELDS)
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in REQUIRED_FIELDS:
        assert field in response_json, f"{field} is missing in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITH_NULL_FIELDS, post_id), "response does not match payload"

@pytest.mark.parametrize("post_id", range(1, 4))
def test_update_post_returns_200_with_wrong_payload_key(base_url, post_id, headers):
    response = update_post(base_url, post_id, headers, PAYLOAD_POST_WITH_WRONG_USERID_KEY)
    wrong_key = "userID"
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    assert wrong_key in response_json, "key userID is missing in json"
    assert "userId" not in response_json, "key userId should not be in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITH_WRONG_USERID_KEY, post_id), "response does not match payload"

@pytest.mark.parametrize("post_id", range(1, 4))
def test_update_post_returns_200_without_required_key(base_url, post_id, headers):
    response = update_post(base_url, post_id, headers, PAYLOAD_POST_WITHOUT_TITLE)
    required_fields = REQUIRED_FIELDS.copy()
    required_fields.remove("title")
    assert response.status_code == 200

    response_json = response.json()
    assert isinstance(response_json, dict), "json should not be empty"

    for field in required_fields:
        assert field in response_json, f"{field} is missing in json"
    
    assert "title" not in response_json, "key title should not be in json"

    assert payload_matches_response(response_json, PAYLOAD_POST_WITHOUT_TITLE, post_id), "response does not match payload"

@pytest.mark.parametrize("post_id", [-1, 0, 9_999_999_999])
def test_delete_post_returns_200_and_empty_json_with_invalid_id(base_url, post_id, headers):
    response = delete_post(base_url, post_id, headers)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json == {}, "json should be empty"

