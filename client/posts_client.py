import requests

ENDPOINT_POSTS = "/posts"

class PostsClient():
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.timeout = 10

    def get_post(self, post_id, timeout=None):
        return self.session.get(f"{self.base_url}{ENDPOINT_POSTS}/{post_id}", timeout=self.timeout)

    def create_post(self, payload, timeout=None):
        return self.session.post(f"{self.base_url}{ENDPOINT_POSTS}", json=payload, timeout=self.timeout)

    def update_post(self, post_id, payload, timeout=None):
        return self.session.put(f"{self.base_url}{ENDPOINT_POSTS}/{post_id}", json=payload, timeout=self.timeout)

    def delete_post(self, post_id, timeout=None):
        return self.session.delete(f"{self.base_url}{ENDPOINT_POSTS}/{post_id}", timeout=self.timeout)

