import pytest
from senscritiquescraper.utils import utils, topchart_utils, work_utils


@pytest.fixture(scope="module")
def topchart_row_movie():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def topchart_row_series():
    url = "https://www.senscritique.com/series/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def topchart_row_videogame():
    url = "https://www.senscritique.com/jeuxvideo/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def topchart_row_book():
    url = "https://www.senscritique.com/livres/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def topchart_row_comic():
    url = "https://www.senscritique.com/bd/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def topchart_row_music():
    url = "https://www.senscritique.com/musique/tops/top100-des-top10"
    soup = utils.get_soup(url)
    row = topchart_utils.get_rows_from_topchart(soup)[0]
    return row


@pytest.fixture(scope="module")
def collection_soup():
    url = "https://www.senscritique.com/34nUBqnQvCSkt/collection/all/all/all/all/all/all/all/all/all/page-1"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_movie():
    url = (
        "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    )
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_track():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_morceaux_de_Georges_Brassens/748276"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_serie():
    url = "https://www.senscritique.com/top/resultats/Les_meilleures_series_avec_une_bande_de_potes/188402"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_game():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_jeux_de_simulation/193221"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_comic():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_albums_d_Asterix/326726"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_book():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_livres_de_fantasy_francaise/2242770"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def survey_album():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_albums_francais_des_annees_1960/685854"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def list_work_soup():
    url = "https://www.senscritique.com/series/oeuvres/Sitcom--14557"
    soup = utils.get_soup(url)
    return soup


@pytest.fixture(scope="module")
def work_object_film():
    url = "https://www.senscritique.com/film/Le_Chant_du_loup/24182360"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_serie():
    url = "https://www.senscritique.com/serie/The_Handmaid_s_Tale/21032442"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_jeu():
    url = "https://www.senscritique.com/jeuvideo/Verdun/10624321"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_jeu2():
    # url = "https://www.senscritique.com/jeuvideo/Verdun/10624321"
    url = "https://www.senscritique.com/jeuvideo/Far_Cry_2/202483"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_livre():
    url = "https://www.senscritique.com/livre/Soif/39651063"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_bd():
    url = "https://www.senscritique.com/bd/La_Fille_de_Vercingetorix_Asterix_tome_38/17954654"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_album():
    url = "https://www.senscritique.com/album/Spiritual_Instinct/40163973"
    work = work_utils.Work(url)
    return work


@pytest.fixture(scope="module")
def work_object_morceau():
    url = "https://www.senscritique.com/morceau/Les_Copains_d_abord/294151"
    work = work_utils.Work(url)
    return work
