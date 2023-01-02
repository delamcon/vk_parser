class ExpiredApiKey(Exception):
    """Expired Api Key"""


class ErrorWithCode(Exception):
    def __init__(self, response_code):
        self.error_code = response_code
        self._validate_code()

    def _validate_code(self):
        if self.error_code == 5:
            raise ExpiredApiKey("Update Api Key")
