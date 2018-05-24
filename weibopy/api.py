from .decorators import get_request
from functools import partial


class API(object):

    EMOTIONS = 'https://api.weibo.com/2/emotions.json'

    def __init__(self, oauth):
        self.oauth = oauth
        self.statuses = Statuses(oauth=self.oauth)

    @get_request
    def emotions(self,
                 type:str='face',
                 language:str='cnname'):
        """
        获取微博官方表情的详细信息

        :param type: 表情类别，face：普通表情、ani：魔法表情、cartoon：动漫表情，默认为face。
        :param language: 语言类别，cnname：简体、twname：繁体，默认为cnname。
        :return:
        """
        ...


class Statuses(object):

    HOME_TIMELINE = 'https://api.weibo.com/2/statuses/home_timeline.json'
    USER_TIMELINE = 'https://api.weibo.com/2/statuses/user_timeline.json'
    REPOST_TIMELINE = 'https://api.weibo.com/2/statuses/repost_timeline.json'
    MENTIONS = 'https://api.weibo.com/2/statuses/mentions.json'
    SHOW = 'https://api.weibo.com/2/statuses/show.json'
    COUNT = 'https://api.weibo.com/2/statuses/count.json'
    GO = 'http://api.weibo.com/2/statuses/go'

    def __init__(self, oauth):
        self.oauth = oauth
        self.get_request = partial(get_request, oauth=self.oauth, )

    @get_request
    def home_timeline(self,
                      since_id:int=0,
                      max_id:int=0,
                      count:int=20,
                      page:int=1,
                      base_app:int=0,
                      feature:int=0,
                      trim_user:int=0):
        """
        获取当前登录用户及其所关注（授权）用户的最新微博

        :param since_id: 若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        :param count: 单页返回的记录条数，最大不超过100，默认为20。
        :param page: 返回结果的页码，默认为1。
        :param base_app: 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        :param feature: 过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        :param trim_user: 返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        :return:
        """
        ...

    @get_request
    def user_timeline(self,
                      uid:int=None,
                      screen_name:str=None,
                      since_id:int=0,
                      max_id:int=0,
                      count:int=20,
                      page:int=1,
                      base_app:int=0,
                      feature:int=0,
                      trim_user:int=0):
        """
        获取某个用户最新发表的微博列表

        :param uid: 需要查询的用户ID。
        :param screen_name: 需要查询的用户昵称。
        :param since_id: 若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        :param count: 单页返回的记录条数，最大不超过100，超过100以100处理，默认为20。
        :param page: 返回结果的页码，默认为1。
        :param base_app: 是否只获取当前应用的数据。0为否（所有数据），1为是（仅当前应用），默认为0。
        :param feature: 过滤类型ID，0：全部、1：原创、2：图片、3：视频、4：音乐，默认为0。
        :param trim_user: 返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。
        :return:
        """

        ...

    @get_request
    def repost_timeline(self,
                        id:int,
                        since_id:int=0,
                        max_id:int=0,
                        count:int=20,
                        page:int=1,
                        filter_by_author:int=0):
        """
        获取指定微博的转发微博列表

        :param id: 需要查询的微博ID。
        :param since_id: 若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        :param count: 单页返回的记录条数，最大不超过200，默认为20。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_author: 作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        :return:
        """
        ...

    @get_request
    def mentions(self,
                 since_id:int=0,
                 max_id:int=0,
                 count:int=20,
                 page:int=1,
                 filter_by_author:int=0,
                 filter_by_source:int=0,
                 filter_by_type:int=0):
        """
        获取最新的提到登录用户的微博列表，即@我的微博

        :param since_id: 若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        :param count: 单页返回的记录条数，最大不超过200，默认为20。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_author: 作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        :param filter_by_source: 来源筛选类型，0：全部、1：来自微博、2：来自微群，默认为0。
        :param filter_by_type: 原创筛选类型，0：全部微博、1：原创的微博，默认为0。
        :return:
        """
        ...

    @get_request
    def show(self, id:int):
        """
        根据微博ID获取单条微博内容

        :param id: 需要获取的微博ID。
        :return:
        """
        ...

    @get_request
    def count(self, ids:str):
        """
        批量获取指定微博的转发数评论数

        :param ids: 需要获取数据的微博ID，多个之间用逗号分隔，最多不超过100个。
        :return:
        """
        ...

    @get_request
    def go(self, uid:int, id:int):
        """
        根据ID跳转到单条微博页

        :param uid: 需要跳转的用户ID。
        :param id: 需要跳转的微博ID。
        :return: None
        """
        ...
