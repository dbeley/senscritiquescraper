import pytest
from senscritique_scraper.utils import scr_utils


@pytest.fixture
def top_row_movie():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


@pytest.fixture
def top_row_series():
    url = "https://www.senscritique.com/series/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


@pytest.fixture
def top_row_videogame():
    url = "https://www.senscritique.com/jeuxvideo/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


@pytest.fixture
def top_row_book():
    url = "https://www.senscritique.com/livres/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


@pytest.fixture
def top_row_comic():
    url = "https://www.senscritique.com/bd/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row


@pytest.fixture
def top_row_music():
    url = "https://www.senscritique.com/musique/tops/top100-des-top10"
    soup = scr_utils.get_soup(url)
    row = scr_utils.get_rows_from_top(soup)[0]
    return row
