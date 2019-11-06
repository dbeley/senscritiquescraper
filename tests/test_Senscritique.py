from senscritiquescraper import Senscritique


def test_collection_filename():
    name = "test"
    if (
        Senscritique.create_collection_filename(name)
        != "export_collection_test.csv"
    ):
        raise AssertionError()

    if (
        Senscritique.create_collection_filename(
            user="ruy2x7gyH6NQR9jPTmA9", ext="csv",
        )
        != "export_collection_ruy2x7gyH6NQR9jPTmA9.csv"
    ):
        raise AssertionError()


def test_collection_filename_ext():
    name = "test"
    if (
        Senscritique.create_collection_filename(name, "xlsx")
        != "export_collection_test.xlsx"
    ):
        raise AssertionError()


def test_category_from_topchart_url():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    if Senscritique.get_category_from_topchart_url(url) != "films":
        raise AssertionError()


def test_topchart_filename():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    if (
        Senscritique.create_topchart_filename(url)
        != "export_topchart_films_top100-des-top10.csv"
    ):
        raise AssertionError()


def test_topchart_filename_ext():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    if (
        Senscritique.create_topchart_filename(url, "xlsx")
        != "export_topchart_films_top100-des-top10.xlsx"
    ):
        raise AssertionError()


def test_survey_filename():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    if Senscritique.create_survey_filename(url) != "export_survey_429176.csv":
        raise AssertionError()


def test_survey_filename_ext():
    url = "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    if (
        Senscritique.create_survey_filename(url, "xlsx")
        != "export_survey_429176.xlsx"
    ):
        raise AssertionError()


def test_list_work_filename():
    url = "https://www.senscritique.com/musique/oeuvres"
    if (
        Senscritique.create_list_work_filename(url)
        != "export_listwork_musique_oeuvres.csv"
    ):
        raise AssertionError()

    url = "https://www.senscritique.com/films/oeuvres/Drame--8655"
    if (
        Senscritique.create_list_work_filename(url)
        != "export_listwork_films_Drame--8655.csv"
    ):
        raise AssertionError()


def test_list_work_filename_ext():
    url = "https://www.senscritique.com/musique/oeuvres"
    if (
        Senscritique.create_list_work_filename(url, "xlsx")
        != "export_listwork_musique_oeuvres.xlsx"
    ):
        raise AssertionError()
