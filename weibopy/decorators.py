from functools import wraps


def get_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        params = {k: v for k, v in locals().items() if v is not None}
        params['access_token'] = self.oauth.access_token
        del params['self']
        resp = self.oauth.get(getattr(self, func.__name__.upper()), params=params)
        return resp.json(), resp.status_code
    return wrapper