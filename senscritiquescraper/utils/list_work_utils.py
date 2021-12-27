import logging
from bs4 import BeautifulSoup, element
from typing import Dict, List, Optional
from . import utils
from .row_utils import (
    movies_utils,
    series_utils,
    books_utils,
    comics_utils,
    music_utils,
    videogames_utils,
)

logger = logging.getLogger(__name__)


def get_list_work_current_page_number(soup: BeautifulSoup) -> Optional[int]:
    """Returns the senscritique page number of a BeautifulSoup object."""
    try:
        page_number = int(soup.find("span", {"class": "eipa-current"}).text)
        logger.info("Current list_work page number : %s", page_number)
        return page_number
    except Exception as e:
        logger.error(f"get_list_work_current_page_number: {e}")
        return None


def get_dict_available_pages(soup: BeautifulSoup) -> Dict[int, str]:
    """Returns a dict of the available pages in a BeautifulSoup object."""
    dict_links = {
        int(x["data-sc-pager-page"]): "https://www.senscritique.com" + x["href"]
        for x in soup.find_all("a", {"class": "eipa-anchor"})
    }
    return dict_links


def get_next_list_work_link(soup: BeautifulSoup) -> Optional[str]:
    """Returns the next link of BeautifulSoup object."""
    available_pages = get_dict_available_pages(soup)
    logger.debug("Available pages : %s.", available_pages)
    current_page = get_list_work_current_page_number(soup)
    if current_page:
        if available_pages.get(current_page + 1):
            return available_pages.get(current_page + 1)
    return None


def get_next_list_work_soup(soup: BeautifulSoup) -> BeautifulSoup:
    """Returns the next BeautifulSoup object for an user list_work."""
    next_col = get_next_list_work_link(soup)
    soup.decompose()
    logger.debug("Next list_work link : %s", next_col)
    if next_col:
        try:
            soup = utils.get_soup(next_col)
        except Exception as e:
            logger.error(e)
            return None
    else:
        return None
    return soup


def get_rows_from_list_work(soup: BeautifulSoup) -> List[element.ResultSet]:
    """Returns a list of rows from a list_work."""
    logger.debug("get_rows_from_list_work")
    list_rows = []
    while True:
        for row in soup.find_all("li", {"class": "elpr-item"}):
            list_rows.append(get_row_infos(row))
        soup = get_next_list_work_soup(soup)
        if not soup:
            logger.debug(
                "No rows here. Either it is the last page, the url is not valid or the list_work is private."
            )
            break
    return list_rows


def get_list_work_infos(soup: BeautifulSoup) -> List[Dict]:
    """Returns a list of dict containing an user list_work information."""
    rows = get_rows_from_list_work(soup)
    return rows


def get_list_work_order():
    """Returns the order of columns for a list_work (not implemented yet)."""
    return None


def get_category(row: element.Tag) -> str:
    return row.find("a", {"class": "elco-anchor"})["href"].split("/")[1]


def get_row_infos(row: element.Tag) -> Optional[Dict]:
    """Returns a dict containing a row information."""
    logger.debug("get_row_infos")
    category = get_category(row)
    if category == "film":
        logger.debug("films")
        row_info = {
            **movies_utils.get_movies_infos_from_row(row),
            **{"Category": "Movie"},
        }
    elif category == "serie":
        logger.debug("series")
        row_info = {
            **series_utils.get_series_infos_from_row(row),
            **{"Category": "Series"},
        }
    elif category == "jeuvideo":
        logger.debug("jeuxvideo")
        row_info = {
            **videogames_utils.get_videogames_infos_from_row(row),
            **{"Category": "Video Game"},
        }
    elif category == "livre":
        logger.debug("livres")
        row_info = {
            **books_utils.get_books_infos_from_row(row),
            **{"Category": "Book"},
        }
    elif category == "bd":
        logger.debug("bd")
        row_info = {
            **comics_utils.get_comics_infos_from_row(row),
            **{"Category": "Comics"},
        }
    elif category == "album":
        logger.debug("musique")
        row_info = {
            **music_utils.get_music_infos_from_row(row),
            **{"Category": "Music"},
        }
    else:
        logger.error(f"Error: unsupported category {category}. Skipping.")
        return None
    row_info.pop("Description", None)
    row_info.pop("Rank", None)
    return row_info
