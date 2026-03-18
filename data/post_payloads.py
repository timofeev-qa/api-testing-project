# positive posts
PAYLOAD_POST_VALID= {
    "userId": 1,
    "title": "test_title_name",
    "body": "test_body_text"
}

# negative posts
PAYLOAD_POST_WITH_NULL_FIELDS = {
    "userId": None,
    "title": None,
    "body": None
}

PAYLOAD_POST_WITH_WRONG_USERID_KEY = {
    "userID": 1,
    "title": "test_title_name",
    "body": "test_body_text"
}

PAYLOAD_POST_WITHOUT_TITLE = {
    "userId": 1,
    "body": "test_body_text"
}
