import pytest
from client.posts_client import PostsClient 
from client.comments_client import CommentsClient

@pytest.fixture
def posts_client():
    return PostsClient()

@pytest.fixture
def comments_client():
    return CommentsClient()