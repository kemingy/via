import base64

from via.utils import http_request_get


URL_IGNORE = "https://api.github.com/repos/github/gitignore/git/trees/main"


def download_file(name):
    files = http_request_get(URL_IGNORE).get("tree", [])
    name = name.lower()

    # find target info
    target = {}
    for lang in files:
        if lang["type"] == "blob" and lang["path"].lower().startswith(name):
            target = lang
            break

    if not target:
        print("Cannot find ignore file of {}.".format(name))
        return

    # download
    data = http_request_get(target["url"])
    if target["sha"] != data["sha"]:
        print("File downloaded is corrupt.")
    else:
        print(base64.b64decode(data.get("content", b"")).decode())
