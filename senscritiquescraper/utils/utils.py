import requests
from bs4 import BeautifulSoup


def get_soup(url: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for an url."""
    return BeautifulSoup(requests.get(url).content, "lxml")


def format_number(number: str) -> str:
    if "K" in number and "." in number:
        return number.replace("K", "").replace(".", "") + "00"
    elif "K" in number and "." not in number:
        return number.replace("K", "") + "000"
    else:
        return number
