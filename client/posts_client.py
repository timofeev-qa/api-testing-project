import requests

ENDPOINT_POSTS = "/posts"

def _make_request(method, endpoint, headers, payload=None):
    return requests.request(method, endpoint, headers=headers, json=payload)

def get_post(base_url, post_id, headers):
    return _make_request("GET", f"{base_url}{ENDPOINT_POSTS}/{post_id}", headers)

def create_post(base_url, headers, payload):
    return _make_request("POST", f"{base_url}{ENDPOINT_POSTS}", headers, payload)

def update_post(base_url, post_id, headers, payload):
    return _make_request("PUT", f"{base_url}{ENDPOINT_POSTS}/{post_id}", headers, payload)

def delete_post(base_url, post_id, headers):
    return _make_request("DELETE", f"{base_url}{ENDPOINT_POSTS}/{post_id}", headers)