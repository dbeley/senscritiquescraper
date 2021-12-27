from senscritiquescraper.utils.row_utils import row_utils


def test_music_rank(topchart_row_music):
    rank = row_utils.get_rank(topchart_row_music)
    if rank != "1":
        raise AssertionError()


def test_music_title(topchart_row_music):
    title = row_utils.get_title(topchart_row_music)
    if title != "The Dark Side of the Moon":
        raise AssertionError()


def test_music_url(topchart_row_music):
    url = row_utils.get_url(topchart_row_music)
    if not url.startswith("https"):
        raise AssertionError()


def test_music_year(topchart_row_music):
    year = row_utils.get_year(topchart_row_music)
    if year != "1973":
        raise AssertionError()


def test_music_release_date(topchart_row_music):
    release_date = row_utils.get_baseline_0(topchart_row_music)
    if release_date != "23 mars 1973":
        print(release_date)
        raise AssertionError()


def test_music_genre(topchart_row_music):
    genre = row_utils.get_baseline_1(topchart_row_music)
    if genre != "Art rock et prog rock":
        raise AssertionError()


def test_music_number_songs(topchart_row_music):
    length = row_utils.get_number_of_seasons(topchart_row_music)
    if length != "10  morceaux":
        raise AssertionError()


def test_music_cover(topchart_row_music):
    cover_url = row_utils.get_picture_url(topchart_row_music)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_music_artist(topchart_row_music):
    artist = row_utils.get_producer(topchart_row_music)
    if artist != "Pink Floyd":
        raise AssertionError()


def test_music_average_rating(topchart_row_music):
    average_rating = row_utils.get_average_rating(topchart_row_music)
    if len(average_rating) != 3:
        raise AssertionError()


def test_music_number_ratings(topchart_row_music):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_music)
    if not int(number_ratings) > 35000:
        raise AssertionError()
