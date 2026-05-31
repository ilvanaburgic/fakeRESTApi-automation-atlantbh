from test_data.authors import AUTHORS_PAYLOAD
from utils.assertions import assert_data_matches_payload, assert_has_keys, assert_valid_json_response
from config import MAX_RESPONSE_TIME


AUTHORS_KEYS = ["id", "idBook", "firstName", "lastName"]


def test_get_all_authors(authors_api):
    response = authors_api.get_all_authors()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], AUTHORS_KEYS)

    assert_valid_json_response(response)


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

    assert_data_matches_payload(data, payload, AUTHORS_KEYS)

    assert_valid_json_response(response)


def test_get_author_book_by_book_id(authors_api, book_id):
    response = authors_api.get_author_book_by_book_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], AUTHORS_KEYS)

    assert data[0]["idBook"] == book_id

    assert_valid_json_response(response)


def test_get_author_by_id(authors_api, author_id):
    response = authors_api.get_author_by_id(author_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, AUTHORS_KEYS)

    assert data["id"] == author_id

    assert_valid_json_response(response)


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

    assert_data_matches_payload(data, payload, AUTHORS_KEYS)

    assert_valid_json_response(response)


def test_delete_author_by_id(authors_api, author_id):
    response = authors_api.delete_author_by_id(author_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME


def test_create_author_without_body(authors_api):
    response = authors_api.create_author_without_body()
    data = response.json()

    assert response.status_code == 400
    assert "A non-empty request body is required." in response.text
    assert isinstance(data, dict)

    assert "application/problem+json" in response.headers["Content-Type"]
    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME
