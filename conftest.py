import pytest
from config import BASE_URL
from clients.activities_api import ActivitiesApi
from clients.authors_api import AuthorsApi
from clients.books_api import BooksApi
from clients.cover_photos_api import CoverPhotosApi
from clients.users_api import UsersApi


@pytest.fixture
def base_url():
    return BASE_URL

@pytest.fixture
def activities_api(base_url):
    return ActivitiesApi(base_url)

@pytest.fixture
def authors_api(base_url):
    return AuthorsApi(base_url)

@pytest.fixture
def books_api(base_url):
    return BooksApi(base_url)

@pytest.fixture
def cover_photos_api(base_url):
    return CoverPhotosApi(base_url)

@pytest.fixture
def users_api(base_url):
    return UsersApi(base_url)

@pytest.fixture
def activity_id():
    return 1

@pytest.fixture
def book_id():
    return 1

@pytest.fixture
def author_id():
    return 1

@pytest.fixture
def cover_photo_id():
    return 1

@pytest.fixture
def user_id():
    return 1

@pytest.fixture
def invalid_activity_id():
    return 10000
