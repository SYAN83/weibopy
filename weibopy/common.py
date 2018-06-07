from .decorators import get_request
from typing import Iterable


class Common(object):
    """
    公共服务接口
    """

    _CODE_TO_LOCATION = 'https://api.weibo.com/2/common/code_to_location.json'
    _GET_CITY = 'https://api.weibo.com/2/common/get_city.json'
    _GET_PROVINCE = 'https://api.weibo.com/2/common/get_province.json'
    _GET_COUNTRY = 'https://api.weibo.com/2/common/get_country.json'
    _GET_TIMEZONE = 'https://api.weibo.com/2/common/get_timezone.json'

    def __init__(self, oauth):
        self.oauth = oauth

    @get_request
    def code_to_location(self, codes: Iterable[str]):
        """
        通过地址编码获取地址名称

        :param codes: 需要查询的地址编码。
        :return: content, status_code
        """
        ...

    @get_request
    def get_city(self,
                 province: str,
                 capital: str=None,
                 language: str='zh-cn'):
        """
        获取城市列表

        :param province: 省份的省份代码。
        :param capital: 城市的首字母，a-z，可为空代表返回全部，默认为全部。
        :param language: 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        :return: content, status_code
        """
        ...

    @get_request
    def get_province(self,
                     country: str,
                     capital: str=None,
                     language: str='zh-cn'):
        """
        获取省份列表

        :param country: 国家的国家代码。
        :param capital: 省份的首字母，a-z，可为空代表返回全部，默认为全部。
        :param language: 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        :return: content, status_code
        """
        ...

    @get_request
    def get_country(self,
                    capital: str=None,
                    language: str='zh-cn'):
        """
        获取国家列表

        :param capital: 国家的首字母，a-z，可为空代表返回全部，默认为全部。
        :param language: 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        :return: content, status_code
        """
        ...

    @get_request
    def get_timezone(self, language: str='zh-cn'):
        """
        获取时区配置表

        :param language: 返回的语言版本，zh-cn：简体中文、zh-tw：繁体中文、english：英文，默认为zh-cn。
        :return: content, status_code
        """
        ...