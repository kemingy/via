import requests
import base64

URL = 'https://api.github.com/repos/github/gitignore/git/trees/master'


def get_all_files():
    try:
        res = requests.get(URL, timeout=5)
    except requests.exceptions.Timeout as err:
        print('Timeout: {}\n Make sure you can connect to GitHub'.format(err))

    if res.status_code == requests.codes.ok:
        try:
            data = res.json()
        except ValueError as err:
            print('Wrong JSON data: {}'.format(err))

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

    # download
    try:
        res = requests.get(target['url'], timeout=5)
    except requests.exceptions.Timeout as err:
        print('Timeout: {}\n Make sure you can connect to GitHub'.format(err))

    if res.status_code == requests.codes.ok:
        try:
            data = res.json()
        except ValueError as err:
            print('Wrong JSON data: {}'.format(err))

        if target['sha'] != data['sha']:
            print('File downloaded is corrupt.')
        else:
            with open('./.gitignore', 'wb') as f:
                f.write(base64.b64decode(data.get('content', b'')))

            print('[{}] ignore file is saved to file ".gitignore".'.format(name))
