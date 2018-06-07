from requests_oauthlib import OAuth2Session
from datetime import datetime


class OAuthHandler(object):
    """
    Weibo authorization handler
    """

    _AUTHORIZE = 'https://api.weibo.com/oauth2/authorize'
    _ACCESS_TOKEN = 'https://api.weibo.com/oauth2/access_token'

    def __init__(self, client_id: str, client_secret: str, redirect_uri: str):
        """
        Initialize OAuthHandler

        :param client_id: 申请应用时分配的AppKey。
        :param client_secret: 申请应用时分配的AppSecret。
        :param redirect_uri: 授权回调地址，站外应用需与设置的回调地址一致，站内应用需填写canvas page的地址。
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def authorize(self):
        """
        Authorization workflow

        :return: OAuth2Session
        """

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
