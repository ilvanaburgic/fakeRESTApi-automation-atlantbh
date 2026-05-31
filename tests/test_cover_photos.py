from test_data.cover_photos import COVER_PHOTOS_PAYLOAD
from utils.assertions import assert_data_matches_payload, assert_has_keys, assert_valid_json_response
from config import MAX_RESPONSE_TIME


COVER_PHOTO_KEYS = ["id", "idBook", "url"]


def test_get_all_cover_photos(cover_photos_api):
    response = cover_photos_api.get_all_cover_photos()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], COVER_PHOTO_KEYS)

    assert_valid_json_response(response)


def test_create_new_cover_photo(cover_photos_api, cover_photo_id, book_id):
    payload = {
        "id": cover_photo_id,
        "idBook": book_id,
        **COVER_PHOTOS_PAYLOAD
    }

    response = cover_photos_api.create_new_cover_photo(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert_has_keys(data, COVER_PHOTO_KEYS)

    assert_data_matches_payload(data, payload, COVER_PHOTO_KEYS)

    assert_valid_json_response(response)


def test_get_cover_photos_by_book_id(cover_photos_api, book_id):
    response = cover_photos_api.get_cover_photos_by_book_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], COVER_PHOTO_KEYS)

    assert data[0]["idBook"] == book_id

    assert_valid_json_response(response)


def test_get_cover_photos_by_id(cover_photos_api, cover_photo_id):
    response = cover_photos_api.get_cover_photos_by_id(cover_photo_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, COVER_PHOTO_KEYS)

    assert data["id"] == cover_photo_id

    assert_valid_json_response(response)


def test_update_cover_photo_by_id(cover_photos_api, cover_photo_id, book_id):
    payload = {
        "id": cover_photo_id,
        "idBook": book_id,
        **COVER_PHOTOS_PAYLOAD
    }

    response = cover_photos_api.update_cover_photo_by_id(cover_photo_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, COVER_PHOTO_KEYS)

    assert_data_matches_payload(data, payload, COVER_PHOTO_KEYS)

    assert_valid_json_response(response)


def test_delete_cover_photo_by_id(cover_photos_api, cover_photo_id):
    response = cover_photos_api.delete_cover_photo_by_id(cover_photo_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < MAX_RESPONSE_TIME
