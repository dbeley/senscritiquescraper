import logging
from .utils import utils, collection_utils, topchart_utils
from typing import List, Dict

logger = logging.getLogger(__name__)


def get_user_collection(user: str = None, url: str = None) -> List[Dict]:
    """Export an user collection in a list of dictionaries.

    Parameters:
        user (str): Username (default is None).
        url (str): Url of the profile page of the user (default is None).

    Returns:
        collection: List of dictionaries containing the user collection.

    """

    if user:
        url = f"https://www.senscritique.com/{user}/collection/all/all/all/all/all/all/all/all/all/page-1"
    if not url:
        raise Exception("user or url not defined")
    logger.info("URL : %s", url)
    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    collection = collection_utils.get_collection_infos(soup)
    return collection


def create_collection_filename(user: str, ext: str = "csv") -> str:
    """Return a filename for a collection."""
    return f"export_collection_{user}.{ext}"


def get_topchart(url: str) -> List[Dict]:
    """Export a topchart from its url in a list of dictionaries.

    Warning: a topchart is different from a survey.
    A topchart is an automatically generated ranking (i.e. Top 111 Films),
    a survey is filled in by the community (i.e. Best Movies for 2013).

    Parameters:
        url (str): Url of the senscritique topchart.

    Returns:
        topchart: List of dictionaries containing the topchart informations.

    """

    logger.info("URL : %s", url)
    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    category = get_category_from_topchart_url(url)
    topchart = topchart_utils.get_topchart_infos(soup, category)
    return topchart


def get_category_from_topchart_url(url: str) -> str:
    """Return the category from an url.

    Throws an error if the url isn't recognized.
    """

    category = url.split("/")[3]
    # check category
    if category not in [
        "films",
        "series",
        "jeuxvideo",
        "livres",
        "bd",
        "musique",
    ]:
        raise Exception(
            "URL malformed. Check that the url contains a Senscritique Top (not a Survey)."
        )
    return category


def create_topchart_filename(url: str, ext: str = "csv") -> str:
    """Return a filename for a topchart."""
    category = get_category_from_topchart_url(url)
    return f"export_topchart_{category}_{url.split('/')[-1]}.{ext}"


def get_survey(url: str) -> List[Dict]:
    """Export a survey from its url in a list of dictionaries.

    Warning: a survey is different from a topchart.
    A topchart is an automatically generated ranking (i.e. Top 111 Films),
    a survey is filled in by the community (i.e. Best Movies for 2013).

    Parameters:
        url (str): Url of the senscritique topchart.

    Returns:
        topchart: List of dictionaries containing the topchart informations.

    """

    logger.info("URL : %s", url)
