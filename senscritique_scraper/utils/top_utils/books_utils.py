import logging
from . import top_row_utils

logger = logging.getLogger(__name__)


def get_books_infos_from_row(row):
    return {
        "Rank": top_row_utils.get_rank(row),
        "Title": top_row_utils.get_title(row),
        "URL": top_row_utils.get_url(row),
        "Original Title": top_row_utils.get_original_title(row),
        "Year": top_row_utils.get_year(row),
        "Release Date": top_row_utils.get_baseline_0(row),
        "Picture URL": top_row_utils.get_picture_url(row),
        "Genre": top_row_utils.get_baseline_1(row),
        "Author": top_row_utils.get_producer(row),
        "Description": top_row_utils.get_description(row),
        "Average Rating": top_row_utils.get_average_rating(row),
        "Number of Ratings": top_row_utils.get_number_of_ratings(row),
    }


def get_order_books_columns():
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
        "Genre",
        "Description",
    ]
