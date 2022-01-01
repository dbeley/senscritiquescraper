from senscritiquescraper.utils.row_utils import row_utils


def test_comic_rank(topchart_row_comic):
    rank = row_utils.get_rank(topchart_row_comic)
    assert rank == "1"


def test_comic_title(topchart_row_comic):
    title = row_utils.get_title(topchart_row_comic)
    assert title == "Watchmen"


def test_comic_url(topchart_row_comic):
    url = row_utils.get_url(topchart_row_comic)
    assert url.startswith("https")


def test_comic_original_title(topchart_row_comic):
    original_title = row_utils.get_original_title(topchart_row_comic)
    assert not original_title


def test_comic_year(topchart_row_comic):
    year = row_utils.get_year(topchart_row_comic)
    assert year == "1986"


def test_comic_release_date(topchart_row_comic):
    release_date = row_utils.get_baseline_0(topchart_row_comic)
    assert release_date == "novembre 1998 (France)"


def test_comic_cover(topchart_row_comic):
    cover_url = row_utils.get_picture_url(topchart_row_comic)
    assert cover_url.startswith("https")


def test_comic_author(topchart_row_comic):
    author = row_utils.get_producer(topchart_row_comic)
    assert author == "Dave Gibbons, Alan Moore"


def test_comic_description(topchart_row_comic):
    description = row_utils.get_description(topchart_row_comic)
    assert description.startswith("Un")


def test_comic_average_rating(topchart_row_comic):
    average_rating = row_utils.get_average_rating(topchart_row_comic)
    assert len(average_rating) == 3


def test_comic_number_ratings(topchart_row_comic):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_comic)
    assert int(number_ratings) > 20000
