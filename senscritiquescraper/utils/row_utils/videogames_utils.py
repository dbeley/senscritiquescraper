import logging
from . import row_utils
from bs4 import element
from typing import List, Dict

logger = logging.getLogger(__name__)


def get_videogames_infos_from_row(row: element.Tag) -> Dict:
    """Returns a dict containing infos for a videogame row."""
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Original Title": row_utils.get_original_title(row),
        "Year": row_utils.get_year(row),
        "Release Date": row_utils.get_baseline_0(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Genre": row_utils.get_baseline_1(row),
        "Developer": row_utils.get_producer(row),
        "Platforms": row_utils.get_platforms(row),
        "Description": row_utils.get_description(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_videogames_columns() -> List:
    """Returns the order of columns for videogames rows."""
    return [
        "Rank",
        "Title",
        "Developer",
        "Platforms",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Original Title",
        "Year",
        "Release Date",
        "Picture URL",
        "Genre",
        "Description",
    ]
