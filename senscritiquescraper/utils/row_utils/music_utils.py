import logging
from . import row_utils

logger = logging.getLogger(__name__)


def get_music_infos_from_row(row):
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Year": row_utils.get_year(row),
        "Release Date": row_utils.get_baseline_0(row),
        "Genre": row_utils.get_baseline_1(row),
        "Number of Songs": row_utils.get_number_of_seasons(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Artist": row_utils.get_producer(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_music_columns():
    return [
        "Rank",
        "Title",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Year",
        "Release Date",
        "Genre",
        "Number of Songs",
        "Picture URL",
        "Artist",
    ]
