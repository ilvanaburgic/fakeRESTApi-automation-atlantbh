def test_get_all_activities(activities_api):
    response = activities_api.get_all_activities()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "title" in data[0]
    assert "dueDate" in data[0]
    assert "completed" in data[0]

    assert data[0]["id"] is not None
    assert data[0]["title"] is not None
    assert data[0]["dueDate"] is not None
    assert data[0]["completed"] is not None

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_activity(activities_api, activity_id):
    payload = {
        "id": activity_id,
        "title": "Test activity 1",
        "dueDate": "2026-05-02T18:52:22.384Z",
        "completed": True
    }

    response = activities_api.create_new_activity(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "dueDate" in data
    assert "completed" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["dueDate"] is not None
    assert data["completed"] is not None

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["dueDate"] == payload["dueDate"]
    assert data["completed"] == payload["completed"]

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_activity_by_id(activities_api, activity_id):
    response = activities_api.get_activity_by_id(activity_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "dueDate" in data
    assert "completed" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["dueDate"] is not None
    assert data["completed"] is not None

    assert data["id"] == activity_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_activity_by_id(activities_api, activity_id):
    payload = {
        "id": activity_id,
        "title": "Test activity 1",
        "dueDate": "2026-05-02T20:47:26.877Z",
        "completed": True
    }

    response = activities_api.update_activity_by_id(activity_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "dueDate" in data
    assert "completed" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["dueDate"] is not None
    assert data["completed"] is not None

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["dueDate"] == payload["dueDate"]
    assert data["completed"] == payload["completed"]

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_activity_by_id(activities_api, activity_id):
    response = activities_api.delete_activity_by_id(activity_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1


def test_get_activity_by_invalid_id(activities_api, invalid_activity_id):
    response = activities_api.get_activity_by_invalid_id(invalid_activity_id)

    assert response.status_code == 404
    assert "Not Found" in response.text

    assert response.elapsed.total_seconds() < 1
