import logging
from . import row_utils
from bs4 import element
from typing import List, Dict

logger = logging.getLogger(__name__)


def get_track_infos_from_row(row: element.Tag) -> Dict:
    """Returns a dict containing infos for a track row."""
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Year": row_utils.get_year(row),
        "Length": row_utils.get_baseline_0(row),
        "Description": row_utils.get_baseline_1(row),
        "Number of Songs": row_utils.get_number_of_seasons(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Artist": row_utils.get_producer(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_track_columns() -> List:
    """Returns the order of columns for track rows."""
    return [
        "Rank",
        "Title",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Year",
        "Length",
        "Description",
        "Number of Songs",
        "Picture URL",
        "Artist",
    ]
