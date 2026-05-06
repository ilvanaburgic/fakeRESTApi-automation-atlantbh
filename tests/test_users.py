from test_data.users import USERS_PAYLOAD


USERS_KEYS = ["id", "userName", "password"]


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data
        assert data[key] is not None


def assert_user_matches_payload(data, payload):
    assert data["id"] == payload["id"]
    assert data["userName"] == payload["userName"]
    assert data["password"] == payload["password"]


def test_get_all_users(users_api):
    response = users_api.get_all_users()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], USERS_KEYS)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_user(users_api, user_id):
    payload = {
        "id": user_id,
        **USERS_PAYLOAD
    }

    response = users_api.create_new_user(payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, USERS_KEYS)

    assert_user_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_user_by_id(users_api, user_id):
    response = users_api.get_user_by_id(user_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, USERS_KEYS)

    assert data["id"] == user_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_user_by_id(users_api, user_id):
    payload = {
        "id": user_id,
        **USERS_PAYLOAD
    }

    response = users_api.update_user_by_id(user_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, USERS_KEYS)

    assert_user_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_user_by_id(users_api, user_id):
    response = users_api.delete_user_by_id(user_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1


def test_get_users_with_invalid_endpoint(users_api):
    response = users_api.get_users_with_invalid_endpoint()

    assert response.status_code == 404
    assert response.text == ""
    assert response.elapsed.total_seconds() < 1
