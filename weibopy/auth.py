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
        # 请求用户授权Token
        self.oauth = OAuth2Session(self.client_id,
                                   redirect_uri=self.redirect_uri)
        authorization_url, state = self.oauth.authorization_url(url=self.AUTHORIZE)

        print('Please load the link {} to your browser and authorize weibo API access.'.format(authorization_url))
        authorization_response = input('Enter the full callback URL:')

        # # TODO: change selenium for remote use
        # # selenium open authorize url
        # driver = webdriver.Chrome()
        # driver.get(authorization_url)
        # # selenium authorize
        # while True:
        #     if driver.current_url.startswith(self.redirect_uri):
        #         authorization_response = driver.current_url
        #         parsed = urlparse(driver.current_url)
        #         print(parse_qs(parsed.query))
        #         driver.close()
        #         break
        #     time.sleep(1)

        # 获取授权过的Access Token
        token = self.oauth.fetch_token(self.ACCESS_TOKEN,
                                       authorization_response=authorization_response,
                                       client_id=self.client_id,
                                       client_secret=self.client_secret)
        print('token: {}'.format(token))
        return self.oauth


if __name__ == '__main__':
    pass