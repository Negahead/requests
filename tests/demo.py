import requests


def request_get():
    r = requests.get('https://github.com/Negahead/requests.git')
    status_code = r.status_code
    print(status_code)


def session_test():
    s = requests.Session()


def CaseInsensitiveDict_test():
    from requests.structures import CaseInsensitiveDict
    c = CaseInsensitiveDict()
    c['name'] = 'dopa'


def cookie_test():
    from requests.models import PreparedRequest
    prepared_request = PreparedRequest()
    prepared_request.prepare(method='GET', url='http://www.baidu.com',cookies={'name': 'Will'})


def auth_test():
    from requests.auth import _basic_auth_str
    s = _basic_auth_str('Negahead', '234234')
    print(s)


if __name__ == '__main__':
    auth_test()
