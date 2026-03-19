# API Testing Project (JSONPlaceholder)

Simple API testing project using `pytest` and `requests` with a client layer.

## Stack
- Python
- pytest
- requests

---

## Structure

- client/ # API clients
- data/ # payloads + shared assertions
- tests/ # test cases
- conftest.py # fixtures (clients)

---

## Architecture

Tests do not call `requests` directly.

tests → client → requests

- clients handle HTTP logic  
- tests focus on validation  
- fixtures provide ready clients  

---

## Covered

### Posts
- GET /posts/{id}
- POST /posts
- PUT /posts/{id}
- DELETE /posts/{id}

### Comments
- GET /comments/{id}
- GET /comments?postId={id}

### Relation
- comments belong to post (postId == post.id)
- invalid post → 404 + empty comments list

---

## Notes

JSONPlaceholder is a mock API:
- no real persistence
- limited validation
- responses may mirror request payload

Tests focus on:
- status codes
- response structure
- filtering behavior
- basic relations

---

## Run
pytest -v