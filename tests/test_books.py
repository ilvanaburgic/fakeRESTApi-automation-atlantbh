def test_get_all_books(books_api):
    response = books_api.get_all_books()
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

    assert "id" in data[0]
    assert "title" in data[0]
    assert "description" in data[0]
    assert "pageCount" in data[0]
    assert "excerpt" in data[0]
    assert "publishDate" in data[0]

    assert data[0]["id"] is not None
    assert data[0]["title"] is not None
    assert data[0]["description"] is not None
    assert data[0]["pageCount"] is not None
    assert data[0]["excerpt"] is not None
    assert data[0]["publishDate"] is not None

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_create_new_book(books_api, book_id):
    payload = {
        "id": book_id,
        "title": "Book 1",
        "description": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem",
        "pageCount": 100,
        "excerpt": "Short summary of the book 1",
        "publishDate": "2026-05-03T11:49:00.522Z"
    }

    response = books_api.create_new_book(payload)
    data = response.json()

    assert response.status_code in [200, 201]
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "pageCount" in data
    assert "excerpt" in data
    assert "publishDate" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["description"] is not None
    assert data["pageCount"] is not None
    assert data["excerpt"] is not None
    assert data["publishDate"] is not None

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["pageCount"] == payload["pageCount"]
    assert data["excerpt"] == payload["excerpt"]
    assert data["publishDate"] == payload["publishDate"]

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_get_book_by_id(books_api, book_id):
    response = books_api.get_book_by_id(book_id)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "pageCount" in data
    assert "excerpt" in data
    assert "publishDate" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["description"] is not None
    assert data["pageCount"] is not None
    assert data["excerpt"] is not None
    assert data["publishDate"] is not None

    assert data["id"] == book_id

    assert response.headers["Content-Type"].startswith("application/json")
    assert response.elapsed.total_seconds() < 1


def test_update_book_by_id(books_api, book_id):
    payload = {
        "id": book_id,
        "title": "Book 1",
        "description": "Occaecati tempora ipsum neque omnis recusandae. Ipsam fuga deserunt eveniet distinctio accusamus voluptate sit quisquam.",
        "pageCount": 321,
        "excerpt": "Short summary of the book 1",
        "publishDate": "2026-05-03T18:07:11.827Z"
    }

    response = books_api.update_book_by_id(book_id, payload)
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)

    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "pageCount" in data
    assert "excerpt" in data
    assert "publishDate" in data

    assert data["id"] is not None
    assert data["title"] is not None
    assert data["description"] is not None
    assert data["pageCount"] is not None
    assert data["excerpt"] is not None
    assert data["publishDate"] is not None

    assert data["id"] == payload["id"]
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["pageCount"] == payload["pageCount"]
    assert data["excerpt"] == payload["excerpt"]
    assert data["publishDate"] == payload["publishDate"]

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
