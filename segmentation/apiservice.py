import requests
from requests.auth import HTTPBasicAuth


class ApiService:

    def __init__(self, username, password):
        self.auth = HTTPBasicAuth(username, password)

    def get(self, url):
        return requests.get(url, auth=self.auth)

    def post(self, url, data, headers):
        return requests.post(url, data, headers=headers, auth=self.auth)
