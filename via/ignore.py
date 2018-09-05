import requests
import base64

from .utils import api_request, parse_json

URL_IGNORE = 'https://api.github.com/repos/github/gitignore/git/trees/master'


def get_all_files():
    res = api_request(URL_IGNORE)
    if res and res.status_code == requests.codes.ok:
        data = parse_json(res)
        return data.get('tree', [])

    return []


def download_file(name):
    files = get_all_files()
    name = name.lower()

    # find target info
    target = {}
    for lang in files:
        if lang['type'] == 'blob' and lang['path'].lower().startswith(name):
            target = lang
            break

    if not target:
        print('Cannot find ignore file of {}.'.format(name))
        return

    # download
    res = api_request(target['url'])
    if res and res.status_code == requests.codes.ok:
        data = parse_json(res)
        if target['sha'] != data['sha']:
            print('File downloaded is corrupt.')
        else:
            with open('./.gitignore', 'wb') as f:
                f.write(base64.b64decode(data.get('content', b'')))

            print('[{}] ignore file is saved to file ".gitignore".'.format(name))
