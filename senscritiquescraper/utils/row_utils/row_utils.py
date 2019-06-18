import logging
from bs4 import element
from typing import List

logger = logging.getLogger(__name__)


def parse_baseline(row: element.Tag) -> List[str]:
    """Parse the baseline tag of a row."""
    try:
        baseline = (
            row.find("p", {"class": "elco-baseline"})
            .text.replace("\n", "")
            .replace("\t", "")
            .split(".")
        )
    except Exception as e:
        logger.error(e)
        baseline = None
    return baseline


def get_baseline_0(row: element.Tag) -> str:
    """Get the first element returned by parse_baseline."""
    try:
        baseline = parse_baseline(row)[0].strip()
    except Exception as e:
        logger.error(e)
        baseline = None
    return baseline


def get_baseline_1(row: element.Tag) -> str:
    """Get the second element returned by parse_baseline."""
    try:
        baseline = parse_baseline(row)[1].strip()
    except Exception as e:
        logger.error(e)
        baseline = None
    return baseline


def get_baseline_2(row: element.Tag) -> str:
    """Get the third element returned by parse_baseline."""
    try:
        baseline = parse_baseline(row)[2].strip()
    except Exception as e:
        logger.error(e)
        baseline = None
    return baseline


def get_rank(row: element.Tag) -> str:
    """Get the rank of a row."""
    try:
        rank = row.find("span", {"class": "elto-rank-item"}).text
    except Exception as e:
        logger.error(e)
        rank = None
    return rank


def get_title(row: element.Tag) -> str:
    """Get the title of a row."""
    try:
        title = row.find("a", {"class": "elco-anchor"}).text.strip()
    except Exception as e:
        logger.error(e)
        title = None
    return title


def get_url(row: element.Tag) -> str:
    """Get the url of a row."""
    try:
        url = (
            "https://www.senscritique.com"
            + row.find("a", {"class": "elco-anchor"})["href"]
        )
    except Exception as e:
        logger.error(e)
        url = None
    return url


def get_original_title(row: element.Tag) -> str:
    """Get the original title of a row."""
    try:
        if row.find("p", {"class": "elco-original-title"}):
            original_title = row.find(
                "p", {"class": "elco-original-title"}
            ).text.strip()
        else:
            original_title = None
    except Exception as e:
        logger.error(e)
        original_title = None
    return original_title


def get_year(row: element.Tag) -> str:
    """Get the release year of a row."""
    try:
        year = (
            row.find("span", {"class": "elco-date"})
            .text.replace("(", "")
            .replace(")", "")
        )
    except Exception as e:
        logger.error(e)
        year = None
    return year


def get_picture_url(row: element.Tag) -> str:
    """Get the picture url of a row."""
    try:
        if row.select("img"):
            try:
                picture_url = row.find("img")["src"]
            except Exception as e:
                logger.debug(e)
                picture_url = row.find("img")["data-original"]
        else:
            picture_url = None
    except Exception as e:
        logger.error(e)
        picture_url = None
    return picture_url


def get_genre(row: element.Tag) -> str:
    """Get the genre of a row."""
    try:
        if not get_number_of_seasons(row):
            genre = parse_baseline(row)[2].strip()
        else:
            genre = parse_baseline(row)[3].strip()
    except Exception as e:
        logger.error(e)
        genre = None
    return genre


def get_producer(row: element.Tag) -> str:
    """Get the producer/author of a row."""
    try:
        if row.find("span", {"class": "elco-baseline-a"}):
            producer = ", ".join(
                [
                    x.text.strip()
                    for x in row.find_all("span", {"class": "elco-baseline-a"})
                ]
            )
        else:
            producer = ", ".join(
                [
                    x.text.strip()
                    for x in row.find_all("a", {"class": "elco-baseline-a"})
                ]
            )
    except Exception as e:
        logger.error("get_producer : %s", e)
        producer = None
    return producer


def get_description(row: element.Tag) -> str:
    """Get the description of a row."""
    try:
        description = row.find("p", {"class": "elco-description"}).text.strip()
    except Exception as e:
        logger.error(e)
        description = None
    return description


def get_average_rating(row: element.Tag) -> str:
    """Get the average rating of a row."""
    try:
        average_rating = row.find("a", {"class": "erra-global"}).text.strip()
    except Exception as e:
        logger.error(e)
        average_rating = None
    return average_rating


def get_number_of_ratings(row: element.Tag) -> str:
    """Get the number of ratings of a row."""
    try:
        number_of_ratings = row.find("a", {"class": "erra-global"})[
            "title"
        ].split()[-2]
    except Exception as e:
        logger.error(e)
        number_of_ratings = None
    return number_of_ratings


def get_number_of_seasons(row: element.Tag) -> str:
    """Get the number of seasons of a row."""
    try:
        number_of_seasons = parse_baseline(row)[2].strip()
        if not any(i.isdigit() for i in number_of_seasons):
            return None
    except Exception as e:
        logger.error(e)
        number_of_seasons = None
    return number_of_seasons


def get_platforms(row: element.Tag) -> str:
    """Get the supported platforms of a row."""
    try:
        platforms = (
            row.find_all("p", {"class": "elco-baseline"})[1]
            .text.split("sur")[-1]
            .strip()
        )
    except Exception as e:
        logger.error(e)
        platforms = None
    return platforms
