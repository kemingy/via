import requests

from .utils import api_request, parse_json

URL_LICENSES = 'https://api.github.com/licenses'

def get_all_licenses():
    res = api_request(URL_LICENSES)
    if res and res.status_code == requests.codes.ok:
        data = parse_json(res)
        return data if data else []

    return []


def download_license(name):
    licenses = get_all_licenses()
    name = name.lower()

    # find target info
    target = {}
    for lcs in licenses:
        if lcs['key'].lower().startswith(name):
            target = lcs
            break

    if not target:
        print('Cannot find "{}" license.'.format(name))
        return

    # download
    res = api_request(target['url'])
    if res and res.status_code == requests.codes.ok:
        data = parse_json(res)
        with open('./LICENSE', 'w', encoding='utf-8') as f:
            f.write(data.get('body', ''))

        print('[{}] License is saved to file "LICENSE".'.format(name))
