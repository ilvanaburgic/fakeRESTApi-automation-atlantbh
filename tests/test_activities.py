from test_data.activities import ACTIVITIES_PAYLOAD
from utils.assertions import assert_data_matches_payload, assert_has_keys, assert_valid_json_response
from config import MAX_RESPONSE_TIME


ACTIVITY_KEYS = ["id", "title", "dueDate", "completed"]


def test_get_all_activities(activities_api):
    response = activities_api.get_all_activities()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], ACTIVITY_KEYS)

    assert_valid_json_response(response)


def test_create_new_activity(activities_api, activity_id):
    payload = {
        "id": activity_id,
        **ACTIVITIES_PAYLOAD
    }

    response = activities_api.create_new_activity(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert_has_keys(data, ACTIVITY_KEYS)

    assert_data_matches_payload(data, payload, ACTIVITY_KEYS)

    assert_valid_json_response(response)


def test_get_activity_by_id(activities_api, activity_id):
    response = activities_api.get_activity_by_id(activity_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, ACTIVITY_KEYS)

    assert data["id"] == activity_id

    assert_valid_json_response(response)


def test_update_activity_by_id(activities_api, activity_id):
    payload = {
        "id": activity_id,
        **ACTIVITIES_PAYLOAD
    }

    response = activities_api.update_activity_by_id(activity_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, ACTIVITY_KEYS)

    assert_data_matches_payload(data, payload, ACTIVITY_KEYS)

    assert_valid_json_response(response)


def test_delete_activity_by_id(activities_api, activity_id):
    response = activities_api.delete_activity_by_id(activity_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME


def test_get_activity_by_invalid_id(activities_api, invalid_activity_id):
    response = activities_api.get_activity_by_id(invalid_activity_id)

    assert response.status_code == 404
    assert "Not Found" in response.text

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME
