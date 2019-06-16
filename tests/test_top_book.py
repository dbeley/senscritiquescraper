from senscritique_scraper.utils.top_utils import top_row_utils


def test_book_rank(top_row_book):
    rank = top_row_utils.get_rank(top_row_book)
    if rank != "1":
        raise AssertionError()


def test_book_title(top_row_book):
    title = top_row_utils.get_title(top_row_book)
    if title != "1984":
        raise AssertionError()


def test_book_url(top_row_book):
    url = top_row_utils.get_url(top_row_book)
    if not url.startswith("https"):
        raise AssertionError()


def test_book_original_title(top_row_book):
    original_title = top_row_utils.get_original_title(top_row_book)
    if not original_title == "Nineteen Eighty-Four":
        raise AssertionError()


def test_book_year(top_row_book):
    year = top_row_utils.get_year(top_row_book)
    if year != "1949":
        raise AssertionError()


def test_book_release_date(top_row_book):
    release_date = top_row_utils.get_baseline_0(top_row_book)
    if release_date != "Sortie : 8 juin 1949":
        raise AssertionError()


def test_book_cover(top_row_book):
    cover_url = top_row_utils.get_picture_url(top_row_book)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_book_genre(top_row_book):
    genre = top_row_utils.get_baseline_1(top_row_book)
    if genre != "Science-fiction et roman":
        raise AssertionError()


def test_book_author(top_row_book):
    author = top_row_utils.get_producer(top_row_book)
    if author != "George Orwell":
        raise AssertionError()


def test_book_description(top_row_book):
    description = top_row_utils.get_description(top_row_book)
    if not description.startswith("De tous les carrefours importants"):
        raise AssertionError()


def test_book_average_rating(top_row_book):
    average_rating = top_row_utils.get_average_rating(top_row_book)
    if len(average_rating) != 3:
        raise AssertionError()


def test_book_number_ratings(top_row_book):
    number_ratings = top_row_utils.get_number_of_ratings(top_row_book)
    if not int(number_ratings) > 60000:
        raise AssertionError()
