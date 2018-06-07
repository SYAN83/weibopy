from .decorators import get_request


class Friendships(object):
    """
    关系读取接口
    """

    _FRIENDS = 'https://api.weibo.com/2/friendships/friends.json'
    _FRIENDS_IDS = 'https://api.weibo.com/2/friendships/friends/ids.json'
    _FOLLOWERS = 'https://api.weibo.com/2/friendships/followers.json'
    _FOLLOWERS_IDS = 'https://api.weibo.com/2/friendships/followers/ids.json'
    _SHOW = 'https://api.weibo.com/2/friendships/show.json'

    def __init__(self, oauth):
        self.oauth = oauth

    @get_request
    def friends(self,
                uid: int=None,
                screen_name: str=None,
                count: int=5,
                cursor: int=0,
                trim_status: int=1):
        """
        获取用户的关注列表

        :param uid: 需要查询的用户UID。
        :param screen_name: 需要查询的用户昵称。
        :param count: 单页返回的记录条数，默认为5，最大不超过5。
        :param cursor: 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        :param trim_status: 返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。

            参数uid与screen_name二者必选其一，且只能选其一；
            uid与screen_name只能为当前授权用户；
            只返回同样授权本应用的用户，非授权用户将不返回；

        :return: content, status_code
        """
        ...

    @get_request
    def friends_ids(self,
                    uid: int=None,
                    screen_name: str=None,
                    count: int=5,
                    cursor: int=0):
        """
        获取用户关注的用户UID列表

        :param uid: 需要查询的用户UID。
        :param screen_name: 需要查询的用户昵称。
        :param count: 单页返回的记录条数，默认为5，最大不超过5。
        :param cursor: 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。

            参数uid与screen_name二者必选其一，且只能选其一；
            uid与screen_name只能为当前授权用户；
            只返回同样授权本应用的用户；

        :return: content, status_code
        """
        ...

    @get_request
    def followers(self,
                  uid: int=None,
                  screen_name: str=None,
                  count: int=5,
                  cursor: int=0,
                  trim_status: int=1):
        """
        获取用户的粉丝列表

        :param uid: 需要查询的用户UID。
        :param screen_name: 需要查询的用户昵称。
        :param count: 单页返回的记录条数，默认为5，最大不超过5。
        :param cursor: 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。
        :param trim_status: 返回值中user字段中的status字段开关，0：返回完整status字段、1：status字段仅返回status_id，默认为1。

            参数uid与screen_name二者必选其一，且只能选其一；
            uid与screen_name只能为当前授权用户；
            只返回同样授权本应用的用户，非授权用户将不返回；

        :return: content, status_code
        """
        ...

    @get_request
    def followers_ids(self,
                      uid: int=None,
                      screen_name: str=None,
                      count: int=5,
                      cursor: int=0):
        """
        获取用户粉丝的用户UID列表

        :param uid: 需要查询的用户UID。
        :param screen_name: 需要查询的用户昵称。
        :param count: 单页返回的记录条数，默认为5，最大不超过5。
        :param cursor: 返回结果的游标，下一页用返回值里的next_cursor，上一页用previous_cursor，默认为0。

            参数uid与screen_name二者必选其一，且只能选其一；
            uid与screen_name只能为当前授权用户；
            只返回同样授权本应用的用户；

        :return: content, status_code
        """
        ...

    @get_request
    def show(self,
             source_id: int=None,
             source_screen_name: str=None,
             target_id: int=None,
             target_screen_name: str=None):
        """
        获取两个用户之间的详细关注关系情况

        :param source_id: 源用户的UID。
        :param source_screen_name: 源用户的微博昵称。
        :param target_id: 目标用户的UID。
        :param target_screen_name: 目标用户的微博昵称。

            参数source_id与source_screen_name二者必选其一，且只能选其一
            参数target_id与target_screen_name二者必选其一，且只能选其一

        :return: content, status_code
        """
        ...
