import requests

class CoverPhotosApi:
    """
    Contains all API requests related to CoverPhotos endpoints.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_cover_photos(self):
        return requests.get(f"{self.base_url}/CoverPhotos")

    def create_new_cover_photo(self, data):
        return requests.post(f"{self.base_url}/CoverPhotos", json=data)

    def get_cover_photos_by_book_id(self, book_id):
        return requests.get(f"{self.base_url}/CoverPhotos/books/covers/{book_id}")

    def get_cover_photos_by_id(self, cover_photo_id):
        return requests.get(f"{self.base_url}/CoverPhotos/{cover_photo_id}")

    def update_cover_photo_by_id(self, cover_photo_id, data):
        return requests.put(f"{self.base_url}/CoverPhotos/{cover_photo_id}", json=data)

    def delete_cover_photo_by_id(self, cover_photo_id):
        return requests.delete(f"{self.base_url}/CoverPhotos/{cover_photo_id}")
