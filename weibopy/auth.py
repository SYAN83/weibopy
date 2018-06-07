from requests_oauthlib import OAuth2Session
from datetime import datetime


class OAuthHandler(object):

    _AUTHORIZE = 'https://api.weibo.com/oauth2/authorize'
    _ACCESS_TOKEN = 'https://api.weibo.com/oauth2/access_token'

    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize(self):

        # 请求用户授权Token
        self.oauth = OAuth2Session(self.client_id,
                                   redirect_uri=self.redirect_uri)
        authorization_url, state = self.oauth.authorization_url(url=self._AUTHORIZE)

        print('Please load the link {} to your browser and authorize weibo API access.'.format(authorization_url))
        authorization_response = input('Enter the full callback URL: ')

        # 获取授权过的Access Token
        token = self.oauth.fetch_token(self._ACCESS_TOKEN,
                                       authorization_response=authorization_response,
                                       client_id=self.client_id,
                                       client_secret=self.client_secret)
        print('UID: {}'.format(token['uid']))
        print('Access Token expires at: {}'.format(datetime.fromtimestamp(token['expires_at']).strftime('%Y/%m/%d %H:%M:%S')))
        return self.oauth
