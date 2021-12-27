from senscritiquescraper.utils.row_utils import row_utils


def test_comic_rank(topchart_row_comic):
    rank = row_utils.get_rank(topchart_row_comic)
    if rank != "1":
        raise AssertionError()


def test_comic_title(topchart_row_comic):
    title = row_utils.get_title(topchart_row_comic)
    if title != "Watchmen":
        raise AssertionError()


def test_comic_url(topchart_row_comic):
    url = row_utils.get_url(topchart_row_comic)
    if not url.startswith("https"):
        raise AssertionError()


def test_comic_original_title(topchart_row_comic):
    original_title = row_utils.get_original_title(topchart_row_comic)
    if original_title:
        raise AssertionError()


def test_comic_year(topchart_row_comic):
    year = row_utils.get_year(topchart_row_comic)
    if year != "1986":
        raise AssertionError()


def test_comic_release_date(topchart_row_comic):
    release_date = row_utils.get_baseline_0(topchart_row_comic)
    if release_date != "novembre 1998 (France)":
        print(release_date)
        raise AssertionError()


def test_comic_cover(topchart_row_comic):
    cover_url = row_utils.get_picture_url(topchart_row_comic)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_comic_author(topchart_row_comic):
    author = row_utils.get_producer(topchart_row_comic)
    if author != "Dave Gibbons, Alan Moore":
        raise AssertionError()


def test_comic_description(topchart_row_comic):
    description = row_utils.get_description(topchart_row_comic)
    if not description.startswith("Un"):
        raise AssertionError()


def test_comic_average_rating(topchart_row_comic):
    average_rating = row_utils.get_average_rating(topchart_row_comic)
    if len(average_rating) != 3:
        raise AssertionError()


def test_comic_number_ratings(topchart_row_comic):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_comic)
    if not int(number_ratings) > 20000:
        raise AssertionError()
