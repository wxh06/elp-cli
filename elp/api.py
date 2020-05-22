from json import loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def _post(mod: str, act: str, args: dict, session: str = ''):
    return urlopen(
        Request(
            f'https://www.elpsh.com/api/{mod}/{act}.ashx',
            urlencode(args).encode(),
            headers={'Cookie': f'ASP.NET_SessionId={session}'}
        )
    )


def post(mod: str, act: str, session: str, args: dict = {}):
    res = loads(_post(mod, act, args, session).read().decode())
    assert res['status'] == 0, res
    return res
