from senscritiquescraper.utils.row_utils import row_utils


def test_book_rank(topchart_row_book):
    rank = row_utils.get_rank(topchart_row_book)
    assert rank == "1"


def test_book_title(topchart_row_book):
    title = row_utils.get_title(topchart_row_book)
    assert title == "1984"


def test_book_url(topchart_row_book):
    url = row_utils.get_url(topchart_row_book)
    assert url.startswith("https")


def test_book_original_title(topchart_row_book):
    original_title = row_utils.get_original_title(topchart_row_book)
    assert original_title == "Nineteen Eighty-Four"


def test_book_year(topchart_row_book):
    year = row_utils.get_year(topchart_row_book)
    assert year == "1949"


def test_book_release_date(topchart_row_book):
    release_date = row_utils.get_baseline_0(topchart_row_book)
    assert release_date == "1 juillet 1950 (France)"


def test_book_cover(topchart_row_book):
    cover_url = row_utils.get_picture_url(topchart_row_book)
    assert cover_url.startswith("https")


def test_book_genre(topchart_row_book):
    genre = row_utils.get_baseline_1(topchart_row_book)
    assert genre == "Roman et science-fiction"


def test_book_author(topchart_row_book):
    author = row_utils.get_producer(topchart_row_book)
    assert author == "George Orwell"


def test_book_description(topchart_row_book):
    description = row_utils.get_description(topchart_row_book)
    assert description.startswith("De tous les carrefours importants")


def test_book_average_rating(topchart_row_book):
    average_rating = row_utils.get_average_rating(topchart_row_book)
    assert len(average_rating) == 3


def test_book_number_ratings(topchart_row_book):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_book)
    assert int(number_ratings) > 60000
