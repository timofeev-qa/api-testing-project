import pytest

def assert_expected_status_code(response_raw, expected_code):
    assert response_raw.status_code == expected_code, f"expected '{expected_code}' does not match actual '{response_raw.status_code}'"

def assert_json_match_expected_fields(response_body, required_fields):
    for field in required_fields:
        assert field in response_body, f"{field} is missing in json"