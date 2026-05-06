from test_data.authors import AUTHORS_PAYLOAD


AUTHORS_KEYS = ["id", "idBook", "firstName", "lastName"]


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data
        assert data[key] is not None


def assert_author_matches_payload(data, payload):
    assert data["id"] == payload["id"]
    assert data["idBook"] == payload["idBook"]
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]


def test_get_all_authors(authors_api):
    response = authors_api.get_all_authors()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], AUTHORS_KEYS)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_author(authors_api, author_id, book_id):
    payload = {
        "id": author_id,
        "idBook": book_id,
        **AUTHORS_PAYLOAD
    }

    response = authors_api.create_new_author(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert_has_keys(data, AUTHORS_KEYS)

    assert_author_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_author_book_by_book_id(authors_api, book_id):
    response = authors_api.get_author_book_by_book_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], AUTHORS_KEYS)

    assert data[0]["idBook"] == book_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_author_by_id(authors_api, author_id):
    response = authors_api.get_author_by_id(author_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, AUTHORS_KEYS)

    assert data["id"] == author_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_author_by_id(authors_api, author_id, book_id):
    payload = {
        "id": author_id,
        "idBook": book_id,
        **AUTHORS_PAYLOAD
    }

    response = authors_api.update_author_by_id(author_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, AUTHORS_KEYS)

    assert_author_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_author_by_id(authors_api, author_id):
    response = authors_api.delete_author_by_id(author_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1


def test_create_author_without_body(authors_api):
    response = authors_api.create_author_without_body()
    data = response.json()

    assert response.status_code == 400
    assert "A non-empty request body is required." in response.text
    assert isinstance(data, dict)
    assert "application/problem+json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 1
