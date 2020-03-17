import requests
import json


def search(keyword):
    response = requests.post('http://relevant-xkcd-backend.herokuapp.com/search', data={'search': keyword}).text
    data = json.loads(response)
    if not data['success']:
        return data['message']
    if not data['results']:
        return None
    return data['results'][0]['url']
