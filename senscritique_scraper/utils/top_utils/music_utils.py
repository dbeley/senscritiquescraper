import logging
from . import top_row_utils

logger = logging.getLogger(__name__)


def get_music_infos_from_row(row):
    return {
        "Rank": top_row_utils.get_rank(row),
        "Title": top_row_utils.get_title(row),
        "URL": top_row_utils.get_url(row),
        "Year": top_row_utils.get_year(row),
        "Release Date": top_row_utils.get_baseline_0(row),
        "Genre": top_row_utils.get_baseline_1(row),
        "Number of Songs": top_row_utils.get_number_of_seasons(row),
        "Picture URL": top_row_utils.get_picture_url(row),
        "Artist": top_row_utils.get_producer(row),
        "Average Rating": top_row_utils.get_average_rating(row),
        "Number of Ratings": top_row_utils.get_number_of_ratings(row),
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
