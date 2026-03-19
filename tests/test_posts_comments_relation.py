import pytest
from client.posts_client import PostsClient
from client.comments_client import CommentsClient
from data.shared_functions import assert_expected_status_code

def assert_relation_between_post_and_comments(post_json, comments_json_list):
    for comments_json_item in comments_json_list:
        assert comments_json_item["postId"] == post_json["id"], f'expected comment postId value "{comments_json_item["postId"]}" does not match actual post postId value "{post_json["id"]}"'


# comments are from post
## positive tests
@pytest.mark.parametrize("post_id", range(1, 3))
def test_get_relation_comments_to_post_by_post_id_returns_filtered_comments(posts_client, comments_client, post_id):
    response_post = posts_client.get_post(post_id)
    assert_expected_status_code(response_post, 200)

    response_comments = comments_client.get_comments_by_post(post_id)
    assert_expected_status_code(response_comments, 200)

    response_post_json = response_post.json()
    response_comments_json_list = response_comments.json()
    assert isinstance(response_comments_json_list, list), "json should be a list"
    assert len(response_comments_json_list) > 0, "list should not be empty"
    assert_relation_between_post_and_comments(response_post_json, response_comments_json_list)

## negative tests
@pytest.mark.parametrize("post_id", [-1, 0])
def test_get_relation_comments_to_post_by_post_id_returns_404_and_empty_list_with_status_code_200(posts_client, comments_client, post_id):
    response_post = posts_client.get_post(post_id)
    assert_expected_status_code(response_post, 404)

    response_comments = comments_client.get_comments_by_post(post_id)
    assert_expected_status_code(response_comments, 200)

    response_comments_json_list = response_comments.json()
    assert isinstance(response_comments_json_list, list), "json should be a list"
    assert response_comments_json_list == [], "list should be empty"
