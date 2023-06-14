from via.utils import http_request_get

URL_LICENSES = "https://api.github.com/licenses"


def download_license(name, print_to_stdout=False):
    licenses = http_request_get(URL_LICENSES)
    name = name.lower()

    # find target info
    target = {}
    for lcs in licenses:
        if lcs["key"].lower().startswith(name):
            target = lcs
            break

    if not target:
        print('Cannot find "{}" license.'.format(name))
        return

    # download
    data = http_request_get(target["url"])
    content = data.get("body", "")

    if print_to_stdout:
        print(content)
    else:
        with open("LICENSE", "w") as f:
            f.write(content)
