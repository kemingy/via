import requests

def api_request(url):
    try:
        res = requests.get(url, timeout=5)
    except requests.exceptions.Timeout as err:
        print('Timeout: {}\n Make sure you can connect to GitHub'.format(err))
        return None

    return res

def parse_json(res):
    try:
        data = res.json()
    except ValueError as err:
        print('Wrong JSON data: {}'.format(err))
        return {}

    return data
