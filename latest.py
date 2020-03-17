from bs4 import BeautifulSoup
import requests


def latest():
    response = requests.get("http://xkcd.com").text
    page = BeautifulSoup(response, 'html.parser')
    permanent = page.find("div", id="middleContainer").find("br").next_element.string
    url_loc = permanent.find("https")
    url = permanent[url_loc:]
    return url
