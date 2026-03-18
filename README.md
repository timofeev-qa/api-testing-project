# API Testing Project (JSONPlaceholder)

Simple API testing project using `pytest` and `requests` with a client layer.

## Overview

This project demonstrates basic API testing approach:

* separation of test logic and HTTP logic
* usage of a client layer (`PostsClient`)
* reusable assertions and fixtures
* parametrized tests

JSONPlaceholder is used as a mock API.
It does not validate input data and does not persist changes, so some negative scenarios are intentionally not covered.

---

## Project Structure

```
api-framework/
├── client/        # API clients (HTTP layer)
├── data/          # test data (payloads)
├── tests/         # test cases
├── conftest.py    # pytest fixtures (client setup)
```

---

## Architecture

Tests do not call `requests` directly.

Flow:

```
tests → client → requests
```

* client layer handles all HTTP requests
* tests focus on validation logic
* pytest fixtures provide ready-to-use client instances

---

## Covered Functionality

### Posts API

* GET `/posts/{id}`
* POST `/posts`
* PUT `/posts/{id}`
* DELETE `/posts/{id}`

Test coverage includes:

* status code validation
* response structure validation
* payload → response consistency (for create/update)
* basic negative cases (invalid IDs where behavior is defined)

---

## Notes

* JSONPlaceholder returns mocked responses
* data is not реально created/updated/deleted
* some responses simply mirror request payload

Because of this:

* strict server-side validation is not tested
* tests focus on response structure and behavior

---

## Requirements

* Python 3.10+
* pytest
* requests

---

## Installation

```
pip install -r requirements.txt
```

---

## Run tests

```
pytest -v
```

---

## Example output

```
tests/test_posts.py ..... PASSED
```
