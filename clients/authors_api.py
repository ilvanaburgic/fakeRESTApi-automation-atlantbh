import requests

class AuthorsApi:
    """
    Contains all API requests related to Authors endpoints.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_authors(self):
        return requests.get(f"{self.base_url}/Authors")

    def create_new_author(self, data):
        return requests.post(f"{self.base_url}/Authors", json=data)

    def get_author_book_by_book_id(self, book_id):
        return requests.get(f"{self.base_url}/Authors/authors/books/{book_id}")

    def get_author_by_id(self, author_id):
        return requests.get(f"{self.base_url}/Authors/{author_id}")

    def update_author_by_id(self, author_id, data):
        return requests.put(f"{self.base_url}/Authors/{author_id}", json=data)

    def delete_author_by_id(self, author_id):
        return requests.delete(f"{self.base_url}/Authors/{author_id}")

    def create_author_without_body(self):
        return requests.post(f"{self.base_url}/Authors", headers={"Content-Type": "application/json", "Accept": "application/json"}, data="")
