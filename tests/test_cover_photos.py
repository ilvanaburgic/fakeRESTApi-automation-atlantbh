from test_data.cover_photos import COVER_PHOTOS_PAYLOAD


COVER_PHOTO_KEYS = ["id", "idBook", "url"]


def assert_has_keys(data, keys):
    for key in keys:
        assert key in data
        assert data[key] is not None


def assert_cover_photo_matches_payload(data, payload):
    assert data["id"] == payload["id"]
    assert data["idBook"] == payload["idBook"]
    assert data["url"] == payload["url"]


def test_get_all_cover_photos(cover_photos_api):
    response = cover_photos_api.get_all_cover_photos()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], COVER_PHOTO_KEYS)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


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

    assert_cover_photo_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_cover_photos_by_book_id(cover_photos_api, book_id):
    response = cover_photos_api.get_cover_photos_by_book_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert_has_keys(data[0], COVER_PHOTO_KEYS)

    assert data[0]["idBook"] == book_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_cover_photos_by_id(cover_photos_api, cover_photo_id):
    response = cover_photos_api.get_cover_photos_by_id(cover_photo_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert_has_keys(data, COVER_PHOTO_KEYS)

    assert data["id"] == cover_photo_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


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

    assert_cover_photo_matches_payload(data, payload)

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_delete_cover_photo_by_id(cover_photos_api, cover_photo_id):
    response = cover_photos_api.delete_cover_photo_by_id(cover_photo_id)

    assert response.status_code == 200
    assert response.text == ""
    assert response.headers.get("Content-Length") == "0"

    assert response.elapsed.total_seconds() < 1
