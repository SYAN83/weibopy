from functools import wraps
from .error import APIError


def get_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        params = {k: v for k, v in locals()['kwargs'].items() if v is not None}
        for k, v in params.items():
            if isinstance(v, list):
                if k.startswith('url_'):
                    params[k] = '&'.join(v)
                else:
                    params[k] = ','.join(v)
        params['access_token'] = self.oauth.access_token
        resp = self.oauth.get(getattr(self, '_' + func.__name__.upper()), params=params)
        if 'error' in resp.json():
            raise APIError(response=resp.json())
        return resp.json(), resp.status_code
    return wrapper
