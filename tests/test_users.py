def test_get_all_users(users_api):
    response = users_api.get_all_users()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "userName" in data[0]
    assert "password" in data[0]

    assert data[0]["id"] is not None
    assert data[0]["userName"] is not None
    assert data[0]["password"] is not None

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_user(users_api, user_id):
    payload = {
        "id": user_id,
        "userName": "test",
        "password": "Test123!",
    }

    response = users_api.create_new_user(payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "userName" in data
    assert "password" in data

    assert data["id"] is not None
    assert data["userName"] is not None
    assert data["password"] is not None

    assert data["id"] == payload["id"]
    assert data["userName"] == payload["userName"]
    assert data["password"] == payload["password"]

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_user_by_id(users_api, user_id):
    response = users_api.get_user_by_id(user_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "userName" in data
    assert "password" in data

    assert data["id"] is not None
    assert data["userName"] is not None
    assert data["password"] is not None

    assert data["id"] == user_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_user_by_id(users_api, user_id):
    payload = {
        "id": user_id,
        "userName": "Syble.Runolfsson",
        "password": "OobO442Yk1HLjJR"
    }

    response = users_api.update_user_by_id(user_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "userName" in data
    assert "password" in data

    assert data["id"] is not None
    assert data["userName"] is not None
    assert data["password"] is not None

    assert data["id"] == payload["id"]
    assert data["userName"] == payload["userName"]
    assert data["password"] == payload["password"]

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
