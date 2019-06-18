import logging
from . import row_utils
from bs4 import element
from typing import List, Dict

logger = logging.getLogger(__name__)


def get_comics_infos_from_row(row: element.Tag) -> Dict:
    """Returns a dict containing infos for a comics row."""
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Original Title": row_utils.get_original_title(row),
        "Year": row_utils.get_year(row),
        "Release Date": row_utils.get_baseline_0(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Author": row_utils.get_producer(row),
        "Description": row_utils.get_description(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_comics_columns() -> List:
    """Returns the order of columns for comics rows."""
    return [
        "Rank",
        "Title",
        "Author",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Original Title",
        "Year",
        "Release Date",
        "Picture URL",
        "Description",
    ]
