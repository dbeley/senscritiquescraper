from senscritiquescraper.utils.row_utils import row_utils


def test_book_rank(topchart_row_book):
    rank = row_utils.get_rank(topchart_row_book)
    if rank != "1":
        raise AssertionError()


def test_book_title(topchart_row_book):
    title = row_utils.get_title(topchart_row_book)
    if title != "1984":
        raise AssertionError()


def test_book_url(topchart_row_book):
    url = row_utils.get_url(topchart_row_book)
    if not url.startswith("https"):
        raise AssertionError()


def test_book_original_title(topchart_row_book):
    original_title = row_utils.get_original_title(topchart_row_book)
    if not original_title == "Nineteen Eighty-Four":
        raise AssertionError()


def test_book_year(topchart_row_book):
    year = row_utils.get_year(topchart_row_book)
    if year != "1949":
        raise AssertionError()


def test_book_release_date(topchart_row_book):
    release_date = row_utils.get_baseline_0(topchart_row_book)
    if release_date != "Sortie : 8 juin 1949":
        raise AssertionError()


def test_book_cover(topchart_row_book):
    cover_url = row_utils.get_picture_url(topchart_row_book)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_book_genre(topchart_row_book):
    genre = row_utils.get_baseline_1(topchart_row_book)
    if genre != "Roman et science-fiction":
        raise AssertionError()


def test_book_author(topchart_row_book):
    author = row_utils.get_producer(topchart_row_book)
    if author != "George Orwell":
        raise AssertionError()


def test_book_description(topchart_row_book):
    description = row_utils.get_description(topchart_row_book)
    if not description.startswith("De tous les carrefours importants"):
        raise AssertionError()


def test_book_average_rating(topchart_row_book):
    average_rating = row_utils.get_average_rating(topchart_row_book)
    if len(average_rating) != 3:
        raise AssertionError()


def test_book_number_ratings(topchart_row_book):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_book)
    if not int(number_ratings) > 60000:
        raise AssertionError()
