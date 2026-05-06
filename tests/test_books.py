from test_data.books import BOOKS_PAYLOAD


BOOK_KEYS = ["id", "title", "description", "pageCount", "excerpt", "publishDate"]


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data
        assert data[key] is not None


def assert_book_matches_payload(data, payload):
    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["pageCount"] == payload["pageCount"]
    assert data["excerpt"] == payload["excerpt"]
    assert data["publishDate"] == payload["publishDate"]


def test_get_all_books(books_api):
    response = books_api.get_all_books()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], BOOK_KEYS)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_book(books_api, book_id):
    payload = {
        "id": book_id,
        **BOOKS_PAYLOAD
    }

    response = books_api.create_new_book(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert_has_keys(data, BOOK_KEYS)
    assert_book_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_book_by_id(books_api, book_id):
    response = books_api.get_book_by_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, BOOK_KEYS)

    assert data["id"] == book_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_book_by_id(books_api, book_id):
    payload = {
        "id": book_id,
        **BOOKS_PAYLOAD
    }

    response = books_api.update_book_by_id(book_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, BOOK_KEYS)

    assert_book_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_book_by_id(books_api, book_id):
    response = books_api.delete_book_by_id(book_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1


def test_update_book_without_body(books_api, book_id):
    response = books_api.update_book_without_body(book_id)
    data = response.json()

    assert isinstance(data, dict)
    assert response.status_code == 400
    assert "A non-empty request body is required." in response.text

    assert "application/problem+json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < 1
