from bs4 import BeautifulSoup
import json
import requests


def find(keyword):
    if keyword.isnumeric():
        url = "https://xkcd.com/" + keyword
        if not check_exists(url):
            raise TypeError
    elif keyword == "latest":
        url = latest()
    elif keyword == "random" or keyword == "rand":
        url = random()
    else:
        url = "My best guess: https://" + search(keyword)
    return url


def search(keyword):
    response = requests.post('http://relevant-xkcd-backend.herokuapp.com/search', data={'search': keyword}).text
    data = json.loads(response)
    if not data['success']:
        return data['message']
    if not data['results']:
        return None
    return data['results'][0]['url']


def latest():
    response = requests.get("http://xkcd.com").text
    page = BeautifulSoup(response, 'html.parser')
    permanent = page.find("div", id="middleContainer").find("br").next_element.string
    url_loc = permanent.find("https")
    url = permanent[url_loc:]
    return url


def check_exists(url):
    response = requests.get(url)
    if response.status_code is not 200:
        return False
    return True


def random():
    response = requests.get("https://c.xkcd.com/random/comic/")
    return response.url
