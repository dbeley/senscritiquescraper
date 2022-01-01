from senscritiquescraper.utils.row_utils import row_utils


def test_movie_rank(topchart_row_movie):
    rank = row_utils.get_rank(topchart_row_movie)
    assert rank == "1"


def test_movie_title(topchart_row_movie):
    title = row_utils.get_title(topchart_row_movie)
    assert title == "Fight Club"


def test_movie_url(topchart_row_movie):
    url = row_utils.get_url(topchart_row_movie)
    assert url.startswith("https")


def test_movie_original_title(topchart_row_movie):
    original_title = row_utils.get_original_title(topchart_row_movie)
    assert not original_title


def test_movie_year(topchart_row_movie):
    year = row_utils.get_year(topchart_row_movie)
    assert year == "1999"


def test_movie_release_date(topchart_row_movie):
    release_date = row_utils.get_baseline_1(topchart_row_movie)
    assert release_date == "10 novembre 1999 (France)"


def test_movie_length(topchart_row_movie):
    length = row_utils.get_baseline_0(topchart_row_movie)
    assert length == "2 h 19 min"


def test_movie_cover(topchart_row_movie):
    cover_url = row_utils.get_picture_url(topchart_row_movie)
    assert cover_url.startswith("https")


def test_movie_genre(topchart_row_movie):
    genre = row_utils.get_genre(topchart_row_movie)
    assert genre == "Drame"


def test_movie_author(topchart_row_movie):
    author = row_utils.get_producer(topchart_row_movie)
    assert author == "David Fincher"


def test_movie_description(topchart_row_movie):
    description = row_utils.get_description(topchart_row_movie)
    # description Fight Club
    assert description.startswith("Insomniaque")


def test_movie_average_rating(topchart_row_movie):
    average_rating = row_utils.get_average_rating(topchart_row_movie)
    assert len(average_rating) == 3


def test_movie_number_ratings(topchart_row_movie):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_movie)
    assert int(number_ratings) > 160000
