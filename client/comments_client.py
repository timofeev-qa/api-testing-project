import requests

ENDPOINT_COMMENTS = "/comments"

class CommentsClient():
    def __init__(self):
        self.session = requests.Session()
        self.base_url = "https://jsonplaceholder.typicode.com"
        self.timeout = 10

    def get_comment(self, comment_id):
        return self.session.get(f"{self.base_url}{ENDPOINT_COMMENTS}/{comment_id}", timeout=self.timeout)

    def get_comments_by_post(self, post_id, timeout=None):
        return self.session.get(f"{self.base_url}{ENDPOINT_COMMENTS}", params={"postId": post_id}, timeout=self.timeout)

