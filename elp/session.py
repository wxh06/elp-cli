import re

from elp.api import _post, post


class Student():

    def __init__(self, session_id: str = None):
        self.session_id = session_id

    def login(self, username: str = None, password: str = None):
        self.session_id = re.search(
            r'ASP\.NET_SessionId=([0-9a-z]+?);',
            _post(
                'user',
                'login',
                {
                    'userName': username,
                    'loginUserType': '1',
                    'password': password,
                    'loginType': 'loginForPwd'
                }
            ).getheader('Set-Cookie')
        ).group(1)

    def __getattr__(self, name):
        match = re.fullmatch(r'([a-z]+)_([a-z_]+)', name)
        if match:
            mod, act = match.groups()

            def _api(**args):
                return post(mod, act, self.session_id, args)
            return _api
        raise AttributeError
