import requests

class ActivitiesApi:
    """
    Contains all API requests related to Activities endpoints.
    """
    def __init__(self, base_url):
        self.base_url = base_url

    def get_all_activities(self):
        return requests.get(f"{self.base_url}/Activities")

    def create_new_activity(self, data):
        return requests.post(f"{self.base_url}/Activities", json=data)

    def get_activity_by_id(self, activity_id):
        return requests.get(f"{self.base_url}/Activities/{activity_id}")

    def update_activity_by_id(self, activity_id, data):
        return requests.put(f"{self.base_url}/Activities/{activity_id}", json=data)

    def delete_activity_by_id(self, activity_id):
        return requests.delete(f"{self.base_url}/Activities/{activity_id}")
