from senscritiquescraper.utils.row_utils import row_utils


def test_series_rank(topchart_row_series):
    rank = row_utils.get_rank(topchart_row_series)
    assert rank == "1"


def test_series_title(topchart_row_series):
    title = row_utils.get_title(topchart_row_series)
    assert title == "Breaking Bad"


def test_series_url(topchart_row_series):
    url = row_utils.get_url(topchart_row_series)
    assert url.startswith("https")


def test_series_original_title(topchart_row_series):
    original_title = row_utils.get_original_title(topchart_row_series)
    assert not original_title


def test_series_year(topchart_row_series):
    year = row_utils.get_year(topchart_row_series)
    assert year == "2008"


def test_series_release_date(topchart_row_series):
    release_date = row_utils.get_baseline_1(topchart_row_series)
    assert release_date == "20 octobre 2009 (France)"


def test_series_number_seasons(topchart_row_series):
    number_of_seasons = row_utils.get_number_of_seasons(topchart_row_series)
    assert number_of_seasons == "5 saisons"


def test_series_cover(topchart_row_series):
    cover_url = row_utils.get_picture_url(topchart_row_series)
    assert cover_url.startswith("https")


def test_series_genre(topchart_row_series):
    genre = row_utils.get_genre(topchart_row_series)
    assert genre == "Policier, drame et thriller"


def test_series_author(topchart_row_series):
    author = row_utils.get_producer(topchart_row_series)
    assert author == "Vince Gilligan"


def test_series_description(topchart_row_series):
    description = row_utils.get_description(topchart_row_series)
    assert description.startswith("Walter White, 50 ans, est professeur")


def test_series_average_rating(topchart_row_series):
    average_rating = row_utils.get_average_rating(topchart_row_series)
    assert len(average_rating) == 3


def test_series_number_ratings(topchart_row_series):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_series)
    assert int(number_ratings) > 104000
