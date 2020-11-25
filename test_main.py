import requests
from src.resourses import Base

params = {
    "test_key": "test_value",
    "Accept": 'application/json'
}


class TestHTTPMethods(Base):
    """
    Simple http methods test on https://httpbin.org/ site with test data.
    Sending requests and asserts 'ok' status code | json content-type
    """

    def test_get_request(self):
        link = 'https://httpbin.org/get'
        self.response = requests.get(link, params=params, timeout=10)
        self.check_response_and_content()
        assert self.response.json()['args']['test_key'] == 'test_value'

    def test_post_request(self):
        link = 'https://httpbin.org/post'
        self.response = requests.post(link, json=params, timeout=10)
        self.check_response_and_content()
        assert self.response.json()['json']['test_key'] == 'test_value'

    def test_put_request(self):
        link = 'https://httpbin.org/put'
        self.response = requests.put(link, json=params, timeout=10)
        self.check_response_and_content()
        assert self.response.json()['json']['test_key'] == 'test_value'

    def test_patch_request(self):
        link = 'https://httpbin.org/patch'
        self.response = requests.patch(link, json=params, timeout=10)
        self.check_response_and_content()
        assert self.response.json()['json']['test_key'] == 'test_value'

    def test_delete_request(self):
        link = 'https://httpbin.org/delete'
        self.response = requests.delete(link, timeout=10)
        assert self.response.ok is True


class TestAuth:
    """
        Simple authorization tests, basic and bearer
        """

    def test_basic_auth(self):
        user, password = 'test', 'testing'
        auth = (user, password)
        link = f'https://httpbin.org//basic-auth/{user}/{password}'
        self.response = requests.get(link, auth=auth, timeout=10)
        assert self.response.ok is True
        assert self.response.headers['Content-Type'] == "application/json"

    def test_bearer_auth(self):
        link = 'https://httpbin.org/bearer'
        headers = {"Authorization": "Bearer MYREALLYLONGTOKENIGOT"}
        self.response = requests.get(link, headers=headers, timeout=10)
        assert self.response.ok is True
        assert self.response.headers['Content-Type'] == "application/json"
