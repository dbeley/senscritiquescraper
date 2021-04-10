import logging
from typing import List, Dict
from bs4 import BeautifulSoup, element


from .row_utils import (
    movies_utils,
    series_utils,
    books_utils,
    comics_utils,
    music_utils,
    videogames_utils,
)

logger = logging.getLogger(__name__)


def get_rows_from_survey(soup: BeautifulSoup) -> List[element.ResultSet]:
    """Returns a list of rows from a survey."""
    return soup.find("ol", {"class": "pvi-list"}).find_all("li", {"class": "elpo-item"})


def get_category_from_survey(soup: BeautifulSoup) -> str:
    return (
        soup.find("li", {"class": "header-navigation-universe-current"})
        .find("a")["href"]
        .split("/")[-1]
    )


def get_survey_infos(soup: BeautifulSoup, category: str) -> List[Dict]:
    """Returns a list of dict containing data of a survey."""
    rows = get_rows_from_survey(soup)
    if category == "films":
        list_infos = [movies_utils.get_movies_infos_from_row(x) for x in rows]
    elif category == "series":
        list_infos = [series_utils.get_series_infos_from_row(x) for x in rows]
    elif category == "jeuxvideo":
        list_infos = [videogames_utils.get_videogames_infos_from_row(x) for x in rows]
    elif category == "livres":
        list_infos = [books_utils.get_books_infos_from_row(x) for x in rows]
    elif category == "bd":
        list_infos = [comics_utils.get_comics_infos_from_row(x) for x in rows]
    elif category == "musique":
        list_infos = [music_utils.get_music_infos_from_row(x) for x in rows]
    else:
        logger.error(f"Category {category} not supported.")
        return []
    return list_infos


def get_survey_order(category: str) -> List:
    """Returns the order of columns for a survey based on its category."""
    if category == "films":
        return movies_utils.get_order_movies_columns()
    elif category == "series":
        return series_utils.get_order_series_columns()
    elif category == "jeuxvideo":
        return videogames_utils.get_order_videogames_columns()
    elif category == "livres":
        return books_utils.get_order_books_columns()
    elif category == "bd":
        return comics_utils.get_order_comics_columns()
    elif category == "musique":
        return music_utils.get_order_music_columns()
    else:
        logger.error(f"Category {category} not supported.")
        return []
