import logging
from .utils import (
    collection_utils,
    list_work_utils,
    search_utils,
    survey_utils,
    topchart_utils,
    utils,
    work_utils,
)
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
        survey: List of dictionaries containing the survey informations.

    """

    logger.info("URL : %s", url)
    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    category = survey_utils.get_category_from_survey(soup)
    survey = survey_utils.get_survey_infos(soup, category)
    return survey


def create_survey_filename(url: str, ext: str = "csv") -> str:
    """Return a filename for a survey."""
    return f"export_survey_{url.split('/')[-1]}.{ext}"


def get_list_work(url: str) -> List[Dict]:
    """Export a list of work from its url in a list of dictionaries.

    Parameters:
        url (str): Url (example : https://www.senscritique.com/films/oeuvres)
        Available urls : - https://www.senscritique.com/films/oeuvres
                         - https://www.senscritique.com/series/oeuvres
                         - https://www.senscritique.com/jeuxvideo/oeuvres
                         - https://www.senscritique.com/livres/oeuvres
                         - https://www.senscritique.com/jeuxvideo/oeuvres
                         - https://www.senscritique.com/musique/oeuvres

    Returns:
        List of dictionaries containing the work informations.
    """

    logger.info("URL : %s", url)
    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    list_work = list_work_utils.get_list_work_infos(soup)
    return list_work


def create_list_work_filename(url: str, ext: str = "csv") -> str:
    """Return a filename for a list of work."""
    category = get_category_from_topchart_url(url)
    return f"export_listwork_{category}_{url.split('/')[-1]}.{ext}"


def get_work_details(url: str) -> Dict:
    """Extract details about a work regardless of its category.

    Returns:
        Dictionary containing the work details.
    """

    logger.info("URL : %s", url)

    work = work_utils.Work(url)
    return work.get_details()


def get_url(search_term: str, rank: int = 1) -> str:
    """Return the first result URL for the search term.
    Rank can be changed (default 1: first result).

    Returns:
        URL of the first result.
    """

    logger.info("Search term: %s", search_term)

    url = search_utils.get_search_url(search_term)

    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    return search_utils.get_search_result(soup, 1)
