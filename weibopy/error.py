
class APIError(Exception):

    def __init__(self, response: dict):
        self.message = response.get('error', 'API error')
