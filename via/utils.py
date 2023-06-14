from http import HTTPStatus

import urllib3


def http_request_get(url):
    resp = urllib3.request(
        "GET",
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    if resp.status != HTTPStatus.OK:
        raise Exception(f"Request failed: code={resp.status} msg={resp.data}")

    return resp.json()
