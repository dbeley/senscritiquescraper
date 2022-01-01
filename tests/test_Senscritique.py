from senscritiquescraper import Senscritique


def test_collection_filename():
    name = "test"
    assert Senscritique.create_collection_filename(name) == "export_collection_test.csv"

    assert (
        Senscritique.create_collection_filename(
            user="ruy2x7gyH6NQR9jPTmA9",
            ext="csv",
        )
        == "export_collection_ruy2x7gyH6NQR9jPTmA9.csv"
    )


def test_collection_filename_ext():
    name = "test"
    assert (
        Senscritique.create_collection_filename(name, "xlsx")
        == "export_collection_test.xlsx"
    )


def test_category_from_topchart_url():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    assert Senscritique.get_category_from_topchart_url(url) == "films"


def test_topchart_filename():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    assert (
        Senscritique.create_topchart_filename(url)
        == "export_topchart_films_top100-des-top10.csv"
    )


def test_topchart_filename_ext():
    url = "https://www.senscritique.com/films/tops/top100-des-top10"
    assert (
        Senscritique.create_topchart_filename(url, "xlsx")
        == "export_topchart_films_top100-des-top10.xlsx"
    )


def test_survey_filename():
    url = (
        "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    )
    assert Senscritique.create_survey_filename(url) == "export_survey_429176.csv"


def test_survey_filename_ext():
    url = (
        "https://www.senscritique.com/top/resultats/Les_meilleurs_films_francais/429176"
    )
    assert (
        Senscritique.create_survey_filename(url, "xlsx") == "export_survey_429176.xlsx"
    )


def test_list_work_filename():
    url = "https://www.senscritique.com/musique/oeuvres"
    assert (
        Senscritique.create_list_work_filename(url)
        == "export_listwork_musique_oeuvres.csv"
    )

    url = "https://www.senscritique.com/films/oeuvres/Drame--8655"
    assert (
        Senscritique.create_list_work_filename(url)
        == "export_listwork_films_Drame--8655.csv"
    )


def test_list_work_filename_ext():
    url = "https://www.senscritique.com/musique/oeuvres"
    assert (
        Senscritique.create_list_work_filename(url, "xlsx")
        == "export_listwork_musique_oeuvres.xlsx"
    )
