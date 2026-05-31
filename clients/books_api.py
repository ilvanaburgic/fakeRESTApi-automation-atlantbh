import requests

class BooksApi:
    """
    Contains all API requests related to Books endpoints.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_books(self):
        return requests.get(f"{self.base_url}/Books")

    def create_new_book(self, data):
        return requests.post(f"{self.base_url}/Books", json=data)

    def get_book_by_id(self, book_id):
        return requests.get(f"{self.base_url}/Books/{book_id}")

    def update_book_by_id(self, book_id, data):
        return requests.put(f"{self.base_url}/Books/{book_id}", json=data)

    def delete_book_by_id(self, book_id):
        return requests.delete(f"{self.base_url}/Books/{book_id}")

    def update_book_without_body(self, book_id):
        return requests.put(f"{self.base_url}/Books/{book_id}", headers={"Content-Type": "application/json"}, data="")
