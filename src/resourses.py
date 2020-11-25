class Base:
    def check_response_and_content(self):
        assert self.response.ok is True
        assert self.response.headers['Content-Type'] == "application/json"
