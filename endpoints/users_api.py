import requests

class UsersApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_users(self):
        return requests.get(f"{self.base_url}/Users")

    def create_new_user(self, data):
        return requests.post(f"{self.base_url}/Users", json=data)

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/Users/{user_id}")

    def update_user_by_id(self, user_id, data):
        return requests.put(f"{self.base_url}/Users/{user_id}", json=data)

    def delete_user_by_id(self, user_id):
        return requests.delete(f"{self.base_url}/Users/{user_id}")

    def get_users_with_invalid_endpoint(self):
        return requests.get(f"{self.base_url}/Usersss")
