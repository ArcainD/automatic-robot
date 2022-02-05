import requests

tok = '.................'
par = {'path': 'random folder'}


def create_folder(token, params=None):
    if params is None:
        params = par
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Accept': 'application/json',
               'Authorization': 'OAuth ' + token}

    response = requests.put(url, headers=headers, params=params)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return response.status_code

    return response.status_code


def clearing_disk():
    url = 'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Accept': 'application/json',
               'Authorization': 'OAuth ' + tok}
    params = {'path': 'random folder',
              'permanently': 'True'}

    response = requests.delete(url, headers=headers, params=params)
    return response
