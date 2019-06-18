import logging
import pandas as pd
from .utils import utils, collection_utils, top_utils

logger = logging.getLogger(__name__)


def get_user_collection(user=None, url=None):
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

    chart_infos = collection_utils.get_collection_infos(soup)
    df = pd.DataFrame(chart_infos)
    # df = df[collection_utils.get_collection_order()]
    return df


def create_collection_filename(user):
    return f"export_collection_{user}.csv"


def get_topchart(url):
    logger.info("URL : %s", url)
    try:
        soup = utils.get_soup(url)
    except Exception as e:
        logger.error(e)
        exit()

    category = top_utils.get_category_from_url(url)
    chart_infos = top_utils.get_top_infos(soup, category)
    df = pd.DataFrame(chart_infos)
    df = df[top_utils.get_top_order(category)]
    return df


def get_category_from_top_url(url):
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


def create_topchart_filename(url):
    category = get_category_from_top_url(url)
    return f"export_top_{category}_{url.split('/')[-1]}.csv"
