from test_data.activities import ACTIVITIES_PAYLOAD


ACTIVITY_KEYS = ["id", "title", "dueDate", "completed"]


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data
        assert data[key] is not None


def assert_activity_matches_payload(data, payload):
    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["dueDate"] == payload["dueDate"]
    assert data["completed"] == payload["completed"]


def test_get_all_activities(activities_api):
    response = activities_api.get_all_activities()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], ACTIVITY_KEYS)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


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

    assert_activity_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_activity_by_id(activities_api, activity_id):
    response = activities_api.get_activity_by_id(activity_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, ACTIVITY_KEYS)

    assert data["id"] == activity_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


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

    assert_activity_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_activity_by_id(activities_api, activity_id):
    response = activities_api.delete_activity_by_id(activity_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1


def test_get_activity_by_invalid_id(activities_api, invalid_activity_id):
    response = activities_api.get_activity_by_id(invalid_activity_id)

    assert response.status_code == 404
    assert "Not Found" in response.text

    assert response.elapsed.total_seconds() < 1
