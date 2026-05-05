def test_get_all_authors(authors_api):
    response = authors_api.get_all_authors()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "idBook" in data[0]
    assert "firstName" in data[0]
    assert "lastName" in data[0]

    assert data[0]["id"] is not None
    assert data[0]["idBook"] is not None
    assert data[0]["firstName"] is not None
    assert data[0]["lastName"] is not None

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_author(authors_api, author_id, book_id):
    payload = {
        "id": author_id,
        "idBook": book_id,
        "firstName": "John",
        "lastName": "Doe",
    }

    response = authors_api.create_new_author(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert "id" in data
    assert "idBook" in data
    assert "firstName" in data
    assert "lastName" in data

    assert data["id"] is not None
    assert data["idBook"] is not None
    assert data["firstName"] is not None
    assert data["lastName"] is not None

    assert data["id"] == payload["id"]
    assert data["idBook"] == payload["idBook"]
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_author_book_by_book_id(authors_api, book_id):
    response = authors_api.get_author_book_by_book_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "idBook" in data[0]
    assert "firstName" in data[0]
    assert "lastName" in data[0]

    assert data[0]["id"] is not None
    assert data[0]["idBook"] is not None
    assert data[0]["firstName"] is not None
    assert data[0]["lastName"] is not None

    assert data[0]["idBook"] == book_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_author_by_id(authors_api, author_id):
    response = authors_api.get_author_by_id(author_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "idBook" in data
    assert "firstName" in data
    assert "lastName" in data

    assert data["id"] is not None
    assert data["idBook"] is not None
    assert data["firstName"] is not None
    assert data["lastName"] is not None

    assert data["id"] == author_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_author_by_id(authors_api, author_id, book_id):
    payload = {
        "id": author_id,
        "idBook": book_id,
        "firstName": "John",
        "lastName": "Doe",
    }

    response = authors_api.update_author_by_id(author_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "idBook" in data
    assert "firstName" in data
    assert "lastName" in data

    assert data["id"] is not None
    assert data["idBook"] is not None
    assert data["firstName"] is not None
    assert data["lastName"] is not None

    assert data["id"] == payload["id"]
    assert data["idBook"] == payload["idBook"]
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]

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
