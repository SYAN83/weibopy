from .decorators import get_request


class Comments(object):
    """
    评论读取接口
    """

    _SHOW = 'https://api.weibo.com/2/comments/show.json'
    _BY_ME = 'https://api.weibo.com/2/comments/by_me.json'
    _TO_ME = 'https://api.weibo.com/2/comments/to_me.json'
    _TIMELINE = 'https://api.weibo.com/2/comments/timeline.json'
    _MENTIONS = 'https://api.weibo.com/2/comments/mentions.json'
    _SHOW_BATCH = 'https://api.weibo.com/2/comments/show_batch.json'

    def __init__(self, oauth):
        self.oauth = oauth

    @get_request
    def show(self,
             id: int,
             since_id: int=0,
             max_id: int=0,
             count: int=20,
             page: int=1,
             filter_by_author: int=0):
        """
        根据微博ID返回某条微博的评论列表

        :param id: 需要查询的微博ID。
        :param since_id: 若指定此参数，则返回ID比since_id大的微博（即比since_id时间晚的微博），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的微博，默认为0。
        :param count: 单页返回的记录条数，最大不超过200，默认为20。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_author: 作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。

            只返回授权用户的评论，非授权用户的评论将不返回

        :return: content, status_code
        """
        ...

    @get_request
    def by_me(self,
              since_id: int=0,
              max_id: int=0,
              count: int=50,
              page: int=1,
              filter_by_source: int=0):
        """
        获取当前登录用户所发出的评论列表

        :param since_id: 若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        :param count: 单页返回的记录条数，默认为50。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_source: 来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。
        :return: content, status_code
        """
        ...

    @get_request
    def to_me(self,
              since_id: int=0,
              max_id: int=0,
              count: int=50,
              page: int=1,
              filter_by_author: int=0,
              filter_by_source: int=0):
        """
        获取当前登录用户所发出的评论列表

        :param since_id: 若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        :param count: 单页返回的记录条数，默认为50。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_author: 作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        :param filter_by_source: 来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。

            只返回授权用户的评论，非授权用户的评论将不返回

        :return: content, status_code
        """
        ...

    @get_request
    def timeline(self,
                 since_id: int=0,
                 max_id: int=0,
                 count: int=20,
                 page: int=1,
                 trim_user: int=0):
        """
        获取当前登录用户的最新评论包括接收到的与发出的

        :param since_id: 若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        :param count: 单页返回的记录条数，默认为50。
        :param page: 返回结果的页码，默认为1。
        :param trim_user: 返回值中user字段开关，0：返回完整user字段、1：user字段仅返回user_id，默认为0。

            只返回授权用户的评论，非授权用户的评论将不返回

        :return: content, status_code
        """
        ...

    @get_request
    def mentions(self,
                 since_id: int=0,
                 max_id: int=0,
                 count: int=50,
                 page: int=1,
                 filter_by_author: int=0,
                 filter_by_source: int=0):
        """
        获取当前登录用户所发出的评论列表

        :param since_id: 若指定此参数，则返回ID比since_id大的评论（即比since_id时间晚的评论），默认为0。
        :param max_id: 若指定此参数，则返回ID小于或等于max_id的评论，默认为0。
        :param count: 单页返回的记录条数，默认为50。
        :param page: 返回结果的页码，默认为1。
        :param filter_by_author: 作者筛选类型，0：全部、1：我关注的人、2：陌生人，默认为0。
        :param filter_by_source: 来源筛选类型，0：全部、1：来自微博的评论、2：来自微群的评论，默认为0。

            只返回授权用户的评论，非授权用户的评论将不返回

        :return: content, status_code
        """
        ...

    @get_request
    def show_batch(self, cids: int):
        """
        根据评论ID批量返回评论信息

        :param cids: 需要查询的批量评论ID，用半角逗号分隔，最大50。
        :return: content, status_code
        """
        ...
