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
    track_utils,
)

logger = logging.getLogger(__name__)


def get_collection_current_page_number(soup: BeautifulSoup) -> Optional[int]:
    """Returns the senscritique page number of a BeautifulSoup object."""
    try:
        page_number = int(soup.find("span", {"class": "eipa-current"}).text)
        logger.info("Current collection page number : %s", page_number)
        return page_number
    except Exception as e:
        logger.error(e)
        return None


def get_dict_available_pages(soup: BeautifulSoup) -> Dict[int, str]:
    """Returns a dict of the available pages in a BeautifulSoup object."""
    dict_links = {
        int(x["data-sc-pager-page"]): "https://www.senscritique.com" + x["href"]
        for x in soup.find_all("a", {"class": "eipa-anchor"})
    }
    return dict_links


def get_next_collection_link(soup: BeautifulSoup) -> Optional[str]:
    """Returns the next link of BeautifulSoup object."""
    available_pages = get_dict_available_pages(soup)
    current_page = get_collection_current_page_number(soup)
    if current_page:
        if available_pages.get(current_page + 1):
            return available_pages.get(current_page + 1)
    return None


def get_next_collection_soup(soup: BeautifulSoup) -> BeautifulSoup:
    """Returns the next BeautifulSoup object for an user collection."""
    next_col = get_next_collection_link(soup)
    logger.debug("Next collection link : %s", next_col)
    if next_col:
        try:
            soup = utils.get_soup(next_col)
        except Exception as e:
            logger.error(e)
            return None
    else:
        return None
    return soup


def get_rows_from_collection(soup: BeautifulSoup) -> List[element.ResultSet]:
    """Returns a list of rows from a collection."""
    logger.debug("get_rows_from_collection")
    list_rows = []
    while True:
        list_rows += soup.find_all("li", {"class": "elco-collection-item"})
        soup = get_next_collection_soup(soup)
        if not soup:
            logger.debug(
                "No rows here. Either it is the last page, the url is not valid or the collection  is private."
            )
            break
    return list_rows


def get_collection_infos(soup: BeautifulSoup) -> List[Dict]:
    """Returns a list of dict containing an user collection information."""
    rows = get_rows_from_collection(soup)
    list_infos = []
    for index, row in enumerate(rows, 1):
        info = get_row_infos(row)
        if info:
            list_infos.append(info)
    return list_infos


def get_collection_order():
    """Returns the order of columns for a collection (not implemented yet)."""
    return None


def get_category(row: element.Tag) -> str:
    return row.find("a", {"class": "elco-anchor"})["href"].split("/")[1]


def get_row_infos(row: element.Tag) -> Optional[Dict]:
    """Returns a dict containing a row information."""
    logger.debug("get_row_infos")
    category = get_category(row)
    if category == "film":
        row_info = {
            **movies_utils.get_movies_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Movie"},
        }
    elif category == "serie":
        row_info = {
            **series_utils.get_series_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Series"},
        }
    elif category == "jeuvideo":
        row_info = {
            **videogames_utils.get_videogames_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Video Game"},
        }
    elif category == "livre":
        row_info = {
            **books_utils.get_books_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Book"},
        }
    elif category == "bd":
        row_info = {
            **comics_utils.get_comics_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Comics"},
        }
    elif category == "album":
        row_info = {
            **music_utils.get_music_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Music"},
        }
    elif category == "morceau":
        row_info = {
            **track_utils.get_track_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Track"},
        }
    else:
        logger.error(f"Category {category} not supported.")
        return None
    # row_info.pop("Description", None)
    # row_info.pop("Rank", None)
    return row_info


def get_complementary_infos_collection(row: element.Tag) -> Dict:
    """Get information specific to a collection row."""
    action = row.find("div", {"class": "elco-collection-rating user"}).find(
        "span", {"class": "elrua-useraction-inner only-child"}
    )

    dict_infos = {}
    if action.find("span", {"class": "eins-wish-list"}):
        dict_infos["User Action"] = "Wishlisted"
    elif action.find("span", {"class": "eins-current"}):
        dict_infos["User Action"] = "In Progress"
    else:
        dict_infos["User Action"] = "Rated"

    dict_infos["Recommended"] = (
        "True" if action.find("span", {"class": "eins-user-recommend"}) else "False"
    )

    dict_infos["User Rating"] = action.text.strip()
    logger.debug(dict_infos)
    return dict_infos
