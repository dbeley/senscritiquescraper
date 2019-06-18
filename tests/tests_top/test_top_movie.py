from senscritiquescraper.utils.row_utils import row_utils


def test_movie_rank(top_row_movie):
    rank = row_utils.get_rank(top_row_movie)
    if rank != "1":
        raise AssertionError()


def test_movie_title(top_row_movie):
    title = row_utils.get_title(top_row_movie)
    if title != "Fight Club":
        raise AssertionError()


def test_movie_url(top_row_movie):
    url = row_utils.get_url(top_row_movie)
    if not url.startswith("https"):
        raise AssertionError()


def test_movie_original_title(top_row_movie):
    original_title = row_utils.get_original_title(top_row_movie)
    if original_title:
        raise AssertionError()


def test_movie_year(top_row_movie):
    year = row_utils.get_year(top_row_movie)
    if year != "1999":
        raise AssertionError()


def test_movie_release_date(top_row_movie):
    release_date = row_utils.get_baseline_1(top_row_movie)
    if release_date != "Sortie : 10 septembre 1999":
        raise AssertionError()


def test_movie_length(top_row_movie):
    length = row_utils.get_baseline_0(top_row_movie)
    if length != "2 h 19 min":
        raise AssertionError()


def test_movie_cover(top_row_movie):
    cover_url = row_utils.get_picture_url(top_row_movie)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_movie_genre(top_row_movie):
    genre = row_utils.get_genre(top_row_movie)
    if genre != "Drame":
        raise AssertionError()


def test_movie_author(top_row_movie):
    author = row_utils.get_producer(top_row_movie)
    if author != "David Fincher":
        raise AssertionError()


def test_movie_description(top_row_movie):
    description = row_utils.get_description(top_row_movie)
    if not description.startswith("La vie"):
        raise AssertionError()


def test_movie_average_rating(top_row_movie):
    average_rating = row_utils.get_average_rating(top_row_movie)
    if len(average_rating) != 3:
        raise AssertionError()


def test_movie_number_ratings(top_row_movie):
    number_ratings = row_utils.get_number_of_ratings(top_row_movie)
    if not int(number_ratings) > 160000:
        raise AssertionError()
