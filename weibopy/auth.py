from requests_oauthlib import OAuth2Session
from selenium import webdriver
from urllib.parse import urlparse, parse_qs

import time


class OAuthHandler(object):

    AUTHORIZE = 'https://api.weibo.com/oauth2/authorize'
    ACCESS_TOKEN = 'https://api.weibo.com/oauth2/access_token'

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize(self):
        self.oauth = OAuth2Session(self.client_id,
                                   redirect_uri=self.redirect_uri)
        authorization_url, state = self.oauth.authorization_url(url=self.AUTHORIZE)
        driver = webdriver.Chrome()
        driver.get(authorization_url)

        while True:
            if driver.current_url.startswith(self.redirect_uri):
                authorization_response = driver.current_url
                parsed = urlparse(driver.current_url)
                print(parse_qs(parsed.query))
                driver.close()
                break
            time.sleep(1)

        token = self.oauth.fetch_token(self.ACCESS_TOKEN,
                                       authorization_response=authorization_response,
                                       client_id=self.client_id,
                                       client_secret=self.client_secret)
        print('token: {}'.format(token))
        return self.oauth



if __name__ == '__main__':
    params = {
        'client_id': r'2748360158',
        'client_secret': r'741e70641e80ec130bfb3c1f8a35d561',
        'redirect_uri': 'https://github.com/SYAN83'
    }

    oauth = OAuthHandler(**params).authorize()
    print(oauth)