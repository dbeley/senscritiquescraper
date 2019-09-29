from senscritiquescraper.utils.row_utils import row_utils


def test_series_rank(topchart_row_series):
    rank = row_utils.get_rank(topchart_row_series)
    if rank != "1":
        raise AssertionError()


def test_series_title(topchart_row_series):
    title = row_utils.get_title(topchart_row_series)
    if title != "Breaking Bad":
        raise AssertionError()


def test_series_url(topchart_row_series):
    url = row_utils.get_url(topchart_row_series)
    if not url.startswith("https"):
        raise AssertionError()


def test_series_original_title(topchart_row_series):
    original_title = row_utils.get_original_title(topchart_row_series)
    if original_title:
        raise AssertionError()


def test_series_year(topchart_row_series):
    year = row_utils.get_year(topchart_row_series)
    if year != "2008":
        raise AssertionError()


def test_series_release_date(topchart_row_series):
    release_date = row_utils.get_baseline_1(topchart_row_series)
    if release_date != "Première diffusion : 20 janvier 2008":
        raise AssertionError()


def test_series_number_seasons(topchart_row_series):
    number_of_seasons = row_utils.get_number_of_seasons(topchart_row_series)
    if number_of_seasons != "5 saisons":
        raise AssertionError()


def test_series_cover(topchart_row_series):
    cover_url = row_utils.get_picture_url(topchart_row_series)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_series_genre(topchart_row_series):
    genre = row_utils.get_genre(topchart_row_series)
    if genre != "Thriller, policier et drame":
        raise AssertionError()


def test_series_author(topchart_row_series):
    author = row_utils.get_producer(topchart_row_series)
    if author != "Vince Gilligan":
        raise AssertionError()


def test_series_description(topchart_row_series):
    description = row_utils.get_description(topchart_row_series)
    if not description.startswith("Walter White, 50 ans, est professeur"):
        raise AssertionError()


def test_series_average_rating(topchart_row_series):
    average_rating = row_utils.get_average_rating(topchart_row_series)
    if len(average_rating) != 3:
        raise AssertionError()


def test_series_number_ratings(topchart_row_series):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_series)
    if not int(number_ratings) > 104000:
        raise AssertionError()
