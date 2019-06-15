import logging
from . import row_utils

logger = logging.getLogger(__name__)


def get_movies_infos_from_row(row):
    # try:
    #     rank = row.find("span", {"class": "elto-rank-item"}).text
    # except Exception as e:
    #     logger.error(e)
    #     rank = None
    # try:
    #     title = row.find("a", {"class": "elco-anchor"}).text.strip()
    # except Exception as e:
    #     logger.error(e)
    #     title = None
    # try:
    #     url = (
    #         "https://www.senscritique.com"
    #         + row.find("a", {"class": "elco-anchor"})["href"]
    #     )
    # except Exception as e:
    #     logger.error(e)
    #     url = None
    # try:
    #     if row.find("p", {"class": "elco-original-title"}):
    #         original_title = row.find(
    #             "p", {"class": "elco-original-title"}
    #         ).text.strip()
    #     else:
    #         original_title = None
    # except Exception as e:
    #     logger.error(e)
    #     original_title = None
    # try:
    #     year = (
    #         row.find("span", {"class": "elco-date"})
    #         .text.replace("(", "")
    #         .replace(")", "")
    #     )
    # except Exception as e:
    #     logger.error(e)
    #     year = None
    # try:
    #     release_date = (
    #         row.find("p", {"class": "elco-baseline"}).find("time").text
    #     )
    # except Exception as e:
    #     logger.error(e)
    #     release_date = None
    # try:
    #     length = (
    #         row.find("p", {"class": "elco-baseline"})
    #         .find("span")
    #         .nextSibling.split(".")[0]
    #         .strip()
    #     )
    # except Exception as e:
    #     logger.error(e)
    #     length = None
    # try:
    #     if row.select("img"):
    #         try:
    #             picture_url = row.find("img")["src"]
    #         except Exception as e:
    #             logger.debug(e)
    #             picture_url = row.find("img")["data-original"]
    #     else:
    #         picture_url = None
    # except Exception as e:
    #     logger.error(e)
    #     picture_url = None
    # try:
    #     genre = " ".join(
    #         row.find("p", {"class": "elco-baseline"})
    #         .text.split(".")[-2]
    #         .split()
    #     )
    # except Exception as e:
    #     logger.error(e)
    #     genre = None
    # try:
    #     producer = row.find("span", {"class": "elco-baseline-a"}).text.strip()
    # except Exception as e:
    #     logger.error(e)
    #     producer = None
    # try:
    #     description = row.find("p", {"class": "elco-description"}).text.strip()
    # except Exception as e:
    #     logger.error(e)
    #     description = None
    # try:
    #     average_rating = row.find("a", {"class": "erra-global"}).text.strip()
    # except Exception as e:
    #     logger.error(e)
    #     average_rating = None
    # try:
    #     number_of_ratings = row.find("a", {"class": "erra-global"})[
    #         "title"
    #     ].split()[-2]
    # except Exception as e:
    #     logger.error(e)
    #     number_of_ratings = None
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Original Title": row_utils.get_original_title(row),
        "Year": row_utils.get_year(row),
        "Release Date": row_utils.get_release_date(row),
        "Length": row_utils.get_length(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Genre": row_utils.get_genre(row),
        "Producer": row_utils.get_producer(row),
        "Description": row_utils.get_description(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_movies_columns():
    return [
        "Rank",
        "Title",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Original Title",
        "Year",
        "Release Date",
        "Length",
        "Picture URL",
        "Genre",
        "Producer",
        "Description",
    ]
