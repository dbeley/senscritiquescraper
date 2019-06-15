import logging
import requests
from bs4 import BeautifulSoup

from . import (
    movies_utils,
    series_utils,
    books_utils,
    comics_utils,
    music_utils,
    videogames_utils,
)

logger = logging.getLogger(__name__)


def get_soup(url):
    return BeautifulSoup(requests.get(url).content, "lxml")


def get_category_from_url(url):
    return url.split("/")[3]


def get_rows_from_top(soup):
    return soup.find("ol", {"class": "elto-list"}).find_all(
        "li", {"class": "elto-item"}
    )


def get_top_infos(soup, category):
    rows = get_rows_from_top(soup)
    if category == "films":
        print("films")
        list_infos = [movies_utils.get_movies_infos_from_row(x) for x in rows]
    elif category == "series":
        print("series")
        list_infos = [series_utils.get_series_infos_from_row(x) for x in rows]
    elif category == "jeuxvideo":
        print("jeuxvideo")
        list_infos = [
            videogames_utils.get_videogames_infos_from_row(x) for x in rows
        ]
    elif category == "livres":
        print("livres")
        list_infos = [books_utils.get_books_infos_from_row(x) for x in rows]
    elif category == "bd":
        print("bd")
        list_infos = [comics_utils.get_comics_infos_from_row(x) for x in rows]
    elif category == "musique":
        print("musique")
        list_infos = [music_utils.get_music_infos_from_row(x) for x in rows]
    else:
        logger.error("ERREUR")
        exit()
    return list_infos


def get_order(category):
    if category == "films":
        print("films")
        return movies_utils.get_order_movies_columns()
    elif category == "series":
        print("series")
        return series_utils.get_order_series_columns()
    elif category == "jeuxvideo":
        print("jeuxvideo")
        return videogames_utils.get_order_videogames_columns()
    elif category == "livres":
        print("livres")
        return books_utils.get_order_books_columns()
    elif category == "bd":
        print("bd")
        return comics_utils.get_order_comics_columns()
    elif category == "musique":
        print("musique")
        return music_utils.get_order_music_columns()
    else:
        logger.error("ERREUR")
        exit()
