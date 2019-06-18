import logging
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


def get_collection_current_page_number(soup):
    try:
        page_number = int(soup.find("span", {"class": "eipa-current"}).text)
        logger.info("Current collection page number : %s", page_number)
        return page_number
    except Exception as e:
        logger.error(e)
        return None


def get_dict_available_pages(soup):
    dict_links = {
        int(x["data-sc-pager-page"]): "https://www.senscritique.com"
        + x["href"]
        for x in soup.find_all("a", {"class": "eipa-anchor"})
    }
    return dict_links


def get_next_collection_link(soup):
    available_pages = get_dict_available_pages(soup)
    current_page = get_collection_current_page_number(soup)
    if current_page:
        if available_pages.get(current_page + 1):
            return available_pages.get(current_page + 1)
    return None


def get_next_collection_soup(soup):
    next_col = get_next_collection_link(soup)
    logger.debug("Next collection link : %s", next_col)
    try:
        soup = utils.get_soup(next_col)
    except Exception as e:
        logger.error(e)
        return None
    return soup


def get_rows_from_collection(soup):
    logger.debug("get_rows_from_collection")
    list_rows = []
    while True:
        list_rows += soup.find_all("li", {"class": "elco-collection-item"})
        soup = get_next_collection_soup(soup)
        if not soup:
            logger.debug("not soup. break")
            break
    return list_rows


def get_collection_infos(soup):
    rows = get_rows_from_collection(soup)
    list_infos = []
    for index, row in enumerate(rows, 1):
        list_infos.append(get_row_infos(row))
    return list_infos


def get_collection_order():
    return None


def get_category(row):
    return row.find("a", {"class": "elco-anchor"})["href"].split("/")[1]


def get_row_infos(row):
    logger.debug("get_row_infos")
    category = get_category(row)
    if category == "film":
        logger.debug("films")
        row_info = {
            **movies_utils.get_movies_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Movie"},
        }
    elif category == "serie":
        logger.debug("series")
        row_info = {
            **series_utils.get_series_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Series"},
        }
    elif category == "jeuvideo":
        logger.debug("jeuxvideo")
        row_info = {
            **videogames_utils.get_videogames_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Video Game"},
        }
    elif category == "livre":
        logger.debug("livres")
        row_info = {
            **books_utils.get_books_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Book"},
        }
    elif category == "bd":
        logger.debug("bd")
        row_info = {
            **comics_utils.get_comics_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Comics"},
        }
    elif category == "album":
        logger.debug("musique")
        row_info = {
            **music_utils.get_music_infos_from_row(row),
            **get_complementary_infos_collection(row),
            **{"Category": "Music"},
        }
    else:
        logger.error("ERREUR")
        return None
    row_info.pop("Description", None)
    row_info.pop("Rank", None)
    return row_info


def get_complementary_infos_collection(row):
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
        True
        if action.find("span", {"class": "eins-user-recommend"})
        else False
    )

    dict_infos["User Rating"] = action.text.strip()
    logger.debug(dict_infos)
    return dict_infos
