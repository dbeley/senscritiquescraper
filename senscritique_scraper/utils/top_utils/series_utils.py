import logging
from . import top_row_utils

logger = logging.getLogger(__name__)


def get_series_infos_from_row(row):
    return {
        "Rank": top_row_utils.get_rank(row),
        "Title": top_row_utils.get_title(row),
        "URL": top_row_utils.get_url(row),
        "Original Title": top_row_utils.get_original_title(row),
        "Year": top_row_utils.get_year(row),
        "Release Date": top_row_utils.get_baseline_1(row),
        "Number of Seasons": top_row_utils.get_number_of_seasons(row),
        "Picture URL": top_row_utils.get_picture_url(row),
        "Genre": top_row_utils.get_genre(row),
        "Producer": top_row_utils.get_producer(row),
        "Description": top_row_utils.get_description(row),
        "Average Rating": top_row_utils.get_average_rating(row),
        "Number of Ratings": top_row_utils.get_number_of_ratings(row),
    }


def get_order_series_columns():
    return [
        "Rank",
        "Title",
        "Producer",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Original Title",
        "Year",
        "Release Date",
        "Number of Seasons",
        "Picture URL",
        "Genre",
        "Description",
    ]
