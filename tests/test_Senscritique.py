from senscritiquescraper import Senscritique


def test_collection_filename():
    name = "test"
    if (
        Senscritique.create_collection_filename(name)
        != "export_collection_test.csv"
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
