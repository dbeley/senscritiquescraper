import pytest
from senscritique_scraper.utils import scr_utils, row_utils


@pytest.fixture
def top_row_movie():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


def test_title(top_row_movie):
    title = row_utils.get_title(top_row_movie)
    if title != "Fight Club":
        raise AssertionError()


def test_year(top_row_movie):
    year = row_utils.get_year(top_row_movie)
    if year != "1999":
        raise AssertionError()
