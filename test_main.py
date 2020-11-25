import requests
from src.resourses import Base


params = {
    "test_key": "test_value",
    "Accept": 'application/json'
          }


class TestHTTPMethods(Base):

    def test_get_request(self):
        link = 'https://httpbin.org/get'
        response = requests.get(link, params=params)
        self.check_response_and_content(response)
        assert response.json()['args']['test_key'] == 'test_value'

    def test_post_request(self):
        link = 'https://httpbin.org/post'
        response = requests.post(link, json=params)
        self.check_response_and_content(response)
        assert response.json()['json']['test_key'] == 'test_value'

    def test_put_request(self):
        link = 'https://httpbin.org/put'
        response = requests.put(link, json=params)
        self.check_response_and_content(response)
        assert response.json()['json']['test_key'] == 'test_value'

    def test_patch_request(self):
        link = 'https://httpbin.org/patch'
        response = requests.patch(link, json=params)
        self.check_response_and_content(response)
        assert response.json()['json']['test_key'] == 'test_value'

    def test_delete_request(self):
        link = 'https://httpbin.org/delete'
        response = requests.delete(link)
        assert response.ok is True


