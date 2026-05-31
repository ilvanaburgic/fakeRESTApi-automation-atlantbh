from config import MAX_RESPONSE_TIME

def assert_has_keys(data, keys):
    """
    Verifies that all expected keys exist in the response data
    and that their values are not None.
    """
    for key in keys:
        assert key in data
        assert data[key] is not None

def assert_data_matches_payload(data, payload, keys):
    """
    Verifies that the values returned by the API
    match the values sent in the request payload.
    """
    for key in keys:
        assert data[key] == payload[key]

def assert_valid_json_response(response):
    """
    Verifies that the response content type is JSON
    and that the response time is within the allowed limit.
    """
    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME