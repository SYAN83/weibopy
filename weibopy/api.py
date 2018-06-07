from .decorators import get_request
from .statuses import Statuses
from .comments import Comments
from .users import Users
from .friendships import Friendships
from .short_url import ShortURL
from .common import Common


class API(object):
    """
    微博API (http://open.weibo.com/wiki/微博API)
    """

    _EMOTIONS = 'https://api.weibo.com/2/emotions.json'

    def __init__(self, oauth):
        self.oauth = oauth
        self.statuses = Statuses(oauth=self.oauth)
        self.comments = Comments(oauth=self.oauth)
        self.users = Users(oauth=self.oauth)
        self.friendships = Friendships(oauth=self.oauth)
        self.short_url = ShortURL(oauth=self.oauth)
        self.common = Common(oauth=self.oauth)

    @get_request
    def emotions(self,
                 type: str='face',
                 language: str='cnname'):
        """
        获取微博官方表情的详细信息

        :param type: 表情类别，face：普通表情、ani：魔法表情、cartoon：动漫表情，默认为face。
        :param language: 语言类别，cnname：简体、twname：繁体，默认为cnname。
        :return: content, status_code
        """
        ...

