# WeiboPy ![HitCount](http://hits.dwyl.io/syan83/weibopy.svg) 

An easy-to-use Python library for accessing the Sina Weibo API.

![Python Version](https://img.shields.io/pypi/pyversions/Django.svg)

## Installation

1. pip Install (bash):

    ```bash
    pip3 install git+https://github.com/SYAN83/weibopy
    ```

2. Local install (bash):

    Clone the repository to your local machine and in the repo's top level execute command:
    
    ```bash
    python3 setup.py install
    ```


## Authorization

Sina Weibo API uses OAuth2 authorization framework. 

To authorize, run the following lines in your python scripts:

```python
import weibopy as wb

client_id = r'**********'
client_secret = r'********************************'
redirect_uri = 'https://***************'

oauth = wb.OAuthHandler(client_id, client_secret, redirect_uri).authorize()
```

Then follow the authorization instruction: 

1. load the authorization URL to the browser 
2. from the browser, authorize weibo API access (your username/password is required).
3. when the page is redirected to the redirect URL, cope the entire URL and paste it to the input box to finish authorization.


## Making GET Requests

WeiboPy follows (almost) the same structure as the Official [Weibo API](http://open.weibo.com/wiki/微博API) GET requests. 

Example: return the user’s 2 latest timeline (http://open.weibo.com/wiki/2/statuses/user_timeline)

```python
api = wb.API(oauth)
data, status = api.statuses.user_timeline(count=2)
# status == 200 for successful GET requests
print(data)
```
