import pytest
from data.shared_functions import assert_expected_status_code, assert_json_match_expected_fields

REQUIRED_FIELDS = ["postId", "id", "name", "email", "body"]


def assert_json_post_id_match_expected_post_id(response_body, post_id):
    assert response_body["postId"] == post_id, f'expected post id "{post_id}" does not match actual "{response_body["postId"]}"'

def assert_json_comment_id_match_expected_comment_id(response_body, comment_id):
    assert response_body["id"] == comment_id, f'expected comment id "{comment_id}" does not match actual "{response_body["id"]}"'


# get comments
## positive tests
@pytest.mark.parametrize("comment_id", range(1, 3))
def test_get_comment_by_id_returns_valid_comment(comments_client, comment_id):
    response = comments_client.get_comment(comment_id)
    assert_expected_status_code(response, 200)

    response_json = response.json()
    assert_json_match_expected_fields(response_json, REQUIRED_FIELDS)
    assert_json_comment_id_match_expected_comment_id(response_json, comment_id)

@pytest.mark.parametrize("post_id", range(1, 3))
def test_get_comments_by_post_id_returns_filtered_comments(comments_client, post_id):
    response = comments_client.get_comments_by_post(post_id)
    assert_expected_status_code(response, 200)

    response_json_list = response.json()
    assert isinstance(response_json_list, list), "json should be a list"
    assert len(response_json_list) > 0, "list should not be empty"
    for json_item in response_json_list:
        assert isinstance(json_item, dict), f"expected type dict does not match actual type '{type(json_item)}'"
        assert_json_match_expected_fields(json_item, REQUIRED_FIELDS)
        assert_json_post_id_match_expected_post_id(json_item, post_id)

## negative tests
@pytest.mark.parametrize("comment_id", [-1, 0])
def test_get_comment_by_id_returns_404_and_empty_json(comments_client, comment_id):
    response = comments_client.get_comment(comment_id)
    assert_expected_status_code(response, 404)

    response_json = response.json()
    assert response_json == {}, "json should be empty"

@pytest.mark.parametrize("post_id", [-1, 0])
def test_get_comments_by_post_id_returns_200_and_empty_list(comments_client, post_id):
    response = comments_client.get_comments_by_post(post_id)
    assert_expected_status_code(response, 200)

    response_json_list = response.json()
    assert response_json_list == [], "list should be empty"
