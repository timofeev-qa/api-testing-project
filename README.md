# API Testing Project with Client Layer (JSONPlaceholder)

A simple API testing project using pytest and requests with a client layer abstraction.

## Notes

JSONPlaceholder is a fake API used for testing purposes.  
It does not persist data changes and often returns the request payload as a response.  
Because of this, some negative validation scenarios are limited.

## Project Structure

api-framework/
├── client/        # HTTP client (wraps requests)
├── data/          # test payloads
├── tests/         # test cases using client functions
├── conftest.py    # base_url fixture

## Architecture

Tests do not call requests directly.

All HTTP calls are handled through a client layer:

tests → client → requests
        ↑
     fixtures

The base URL is provided via pytest fixture in conftest.py.
This improves readability and makes tests easier to maintain.

Client layer centralizes HTTP logic and simplifies test maintenance.

Requests include basic headers (Content-Type: application/json) to simulate real API behavior.

## Covered Endpoints

- POST /posts
- GET /posts/{id}
- PUT /posts/{id}
- DELETE /posts/{id}

## Requirements

Python 3.10+
pytest
requests

## Installation

pip install -r requirements.txt

## Run tests

pytest -v

## Example

(venv) PS ...\api-framework> pytest tests/test_posts.py -v
================================================== test session starts ==================================================
...
collected 31 items                                                                                                       

...
tests/test_posts.py::test_update_post_returns_200_without_required_key[2] PASSED                                   [ 87%]
tests/test_posts.py::test_update_post_returns_200_without_required_key[3] PASSED                                   [ 90%]
tests/test_posts.py::test_delete_post_returns_200_and_empty_json_with_invalid_id[-1] PASSED                        [ 93%]
tests/test_posts.py::test_delete_post_returns_200_and_empty_json_with_invalid_id[0] PASSED                         [ 96%]
tests/test_posts.py::test_delete_post_returns_200_and_empty_json_with_invalid_id[9999999999] PASSED                [100%]

================================================== 31 passed in 28.41s ==================================================