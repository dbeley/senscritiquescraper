import logging
from . import top_row_utils

logger = logging.getLogger(__name__)


def get_videogames_infos_from_row(row):
    return {
        "Rank": top_row_utils.get_rank(row),
        "Title": top_row_utils.get_title(row),
        "URL": top_row_utils.get_url(row),
        "Original Title": top_row_utils.get_original_title(row),
        "Year": top_row_utils.get_year(row),
        "Release Date": top_row_utils.get_baseline_0(row),
        "Picture URL": top_row_utils.get_picture_url(row),
        "Genre": top_row_utils.get_baseline_1(row),
        "Developer": top_row_utils.get_producer(row),
        "Platforms": top_row_utils.get_platforms(row),
        "Description": top_row_utils.get_description(row),
        "Average Rating": top_row_utils.get_average_rating(row),
        "Number of Ratings": top_row_utils.get_number_of_ratings(row),
    }


def get_order_videogames_columns():
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
