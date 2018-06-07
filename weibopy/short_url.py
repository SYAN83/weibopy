from .decorators import get_request
from typing import Iterable


class ShortURL(object):
    """
    短链接口
    """

    _SHORTEN = 'https://api.weibo.com/2/short_url/shorten.json'
    _EXPAND = 'https://api.weibo.com/2/short_url/expand.json'
    _SHARE_COUNTS = 'https://api.weibo.com/2/short_url/share/counts.json'
    _COMMENT_COUNTS = 'https://api.weibo.com/2/short_url/comment/counts.json'

    def __init__(self, oauth):
        self.oauth = oauth

    @get_request
    def shorten(self, url_long: Iterable[str]):
        """
        将一个或多个长链接转换成短链接

        :param url_long: 需要转换的长链接，需要URLencoded，最多不超过20个。
        :return: content, status_code
        """

    @get_request
    def expand(self, url_short: Iterable[str]):
        """
        将一个或多个短链接还原成原始的长链接

        :param url_short: 需要还原的短链接，需要URLencoded，最多不超过20个 。
        :return: content, status_code
        """

    @get_request
    def share_counts(self, url_short: Iterable[str]):
        """
        获取短链接在微博上的微博分享数

        :param url_short: 需要取得分享数的短链接，需要URLencoded，最多不超过20个。
        :return: content, status_code
        """
        ...

    @get_request
    def comment_counts(self, url_short: Iterable[str]):
        """
        获取短链接在微博上的微博评论数

        :param url_short: 需要取得分享数的短链接，需要URLencoded，最多不超过20个。
        :return: content, status_code
        """