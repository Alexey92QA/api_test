import requests
from jsonschema import validate


class start_url:
    def __init__(self, url):
        self.url = url

    get_endpoint = '/planetary/apod'

    def create_url(self, param: dict, schema: dict):

        response = requests.get(f"{self.url}{self.get_endpoint}", params=param)
        validate(instance=response.json(), schema=schema)
        return response
