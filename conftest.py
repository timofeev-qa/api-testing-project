import pytest
from client.posts_client import PostsClient

@pytest.fixture
def posts_client():
    return PostsClient()