import requests
from bs4 import BeautifulSoup


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")
