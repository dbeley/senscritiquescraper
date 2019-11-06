import pytest
from senscritiquescraper.utils import utils, topchart_utils


@pytest.fixture
def topchart_row_movie():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def topchart_row_series():
    url = "https://www.senscritique.com/series/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def topchart_row_videogame():
    url = "https://www.senscritique.com/jeuxvideo/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def topchart_row_book():
    url = "https://www.senscritique.com/livres/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def topchart_row_comic():
    url = "https://www.senscritique.com/bd/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def topchart_row_music():
    url = "https://www.senscritique.com/musique/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture
def collection_soup():
    url = "https://www.senscritique.com/34nUBqnQvCSkt/collection/all/all/all/all/all/all/all/all/all/page-1"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture
def survey_soup():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    soup = utils.get_soup(url)
    return soup
