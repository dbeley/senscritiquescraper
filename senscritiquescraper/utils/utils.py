import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for an url."""
    return BeautifulSoup(requests.get(url).content, "lxml")
