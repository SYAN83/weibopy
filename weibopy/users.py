from .decorators import get_request
from typing import Iterable


class Users(object):
    """
    用户读取接口
    """

    _SHOW = 'https://api.weibo.com/2/users/show.json'
    _DOMAIN_SHOW = 'https://api.weibo.com/2/users/domain_show.json'
    _COUNTS = 'https://api.weibo.com/2/users/counts.json'

    def __init__(self, oauth):
        self.oauth = oauth

    @get_request
    def show(self, uid: int=None, screen_name: str=None):
        """
        根据用户ID获取用户信息

        :param uid: 需要查询的用户ID。
        :param screen_name: 需要查询的用户昵称。

            参数uid与screen_name二者必选其一，且只能选其一

        :return: content, status_code
        """
        ...

    @get_request
    def domain_show(self, domain: str):
        """
        通过个性化域名获取用户资料以及用户最新的一条微博

        :param domain: 需要查询的个性化域名。
        :return: content, status_code
        """
        ...

    @get_request
    def counts(self, uids: Iterable[str]):
        """
        批量获取用户的粉丝数、关注数、微博数

        :param uids: 需要获取数据的用户UID，最多不超过100个。
        :return: content, status_code
        """
        ...

