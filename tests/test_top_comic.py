from senscritique_scraper.utils.top_utils import top_row_utils


def test_comic_rank(top_row_comic):
    rank = top_row_utils.get_rank(top_row_comic)
    if rank != "1":
        raise AssertionError()


def test_comic_title(top_row_comic):
    title = top_row_utils.get_title(top_row_comic)
    if title != "Watchmen":
        raise AssertionError()


def test_comic_url(top_row_comic):
    url = top_row_utils.get_url(top_row_comic)
    if not url.startswith("https"):
        raise AssertionError()


def test_comic_original_title(top_row_comic):
    original_title = top_row_utils.get_original_title(top_row_comic)
    if original_title:
        raise AssertionError()


def test_comic_year(top_row_comic):
    year = top_row_utils.get_year(top_row_comic)
    if year != "1986":
        raise AssertionError()


def test_comic_release_date(top_row_comic):
    release_date = top_row_utils.get_baseline_0(top_row_comic)
    if release_date != "Sortie : septembre 1986":
        raise AssertionError()


def test_comic_cover(top_row_comic):
    cover_url = top_row_utils.get_picture_url(top_row_comic)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_comic_author(top_row_comic):
    author = top_row_utils.get_producer(top_row_comic)
    if author != "Dave Gibbons, Alan Moore":
        raise AssertionError()


def test_comic_description(top_row_comic):
    description = top_row_utils.get_description(top_row_comic)
    if not description.startswith("Un"):
        raise AssertionError()


def test_comic_average_rating(top_row_comic):
    average_rating = top_row_utils.get_average_rating(top_row_comic)
    if len(average_rating) != 3:
        raise AssertionError()


def test_comic_number_ratings(top_row_comic):
    number_ratings = top_row_utils.get_number_of_ratings(top_row_comic)
    if not int(number_ratings) > 20000:
        raise AssertionError()
