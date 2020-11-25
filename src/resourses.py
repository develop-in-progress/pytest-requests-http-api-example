import requests


class Base:

    @staticmethod
    def check_response_and_content(response):
        assert response.ok is True
        assert response.headers['Content-Type'] == "application/json"
