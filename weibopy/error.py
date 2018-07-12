
class APIError(Exception):

    def __init__(self, response: dict):
        self.error = response.get('error', 'API error')
        self.error_code = response.get('error_code', 1)
        self.request = response.get('request', '')

    def __str__(self):
        return '{} ({})'.format(self.error, self.error_code)

    def __repr__(self):
        return 'Error: {} Code: {}'.format(self.error, self.error_code)