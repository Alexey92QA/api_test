from jsonschema import validate
from apod.request import Client
from apod.models import ResponseModel


class start_url:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    get_endpoint = '/planetary/apod'

    def create_url(self, param: dict, schema: dict):
        response = self.client.custom_request('GET', f'{self.url}{self.get_endpoint}', params=param)
        validate(instance=response.json(), schema=schema)
        return ResponseModel(status=response.status_code, response=response.json())
