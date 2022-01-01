from senscritiquescraper.utils.row_utils import row_utils


def test_music_rank(topchart_row_music):
    rank = row_utils.get_rank(topchart_row_music)
    assert rank == "1"


def test_music_title(topchart_row_music):
    title = row_utils.get_title(topchart_row_music)
    assert title == "The Dark Side of the Moon"


def test_music_url(topchart_row_music):
    url = row_utils.get_url(topchart_row_music)
    assert url.startswith("https")


def test_music_year(topchart_row_music):
    year = row_utils.get_year(topchart_row_music)
    assert year == "1973"


def test_music_release_date(topchart_row_music):
    release_date = row_utils.get_baseline_0(topchart_row_music)
    assert release_date == "23 mars 1973"


def test_music_genre(topchart_row_music):
    genre = row_utils.get_baseline_1(topchart_row_music)
    assert genre == "Art rock et prog rock"


def test_music_number_songs(topchart_row_music):
    length = row_utils.get_number_of_seasons(topchart_row_music)
    assert length == "10  morceaux"


def test_music_cover(topchart_row_music):
    cover_url = row_utils.get_picture_url(topchart_row_music)
    assert cover_url.startswith("https")


def test_music_artist(topchart_row_music):
    artist = row_utils.get_producer(topchart_row_music)
    assert artist == "Pink Floyd"


def test_music_average_rating(topchart_row_music):
    average_rating = row_utils.get_average_rating(topchart_row_music)
    assert len(average_rating) == 3


def test_music_number_ratings(topchart_row_music):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_music)
    assert int(number_ratings) > 35000
