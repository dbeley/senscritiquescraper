from senscritique_scraper.utils import scr_collection_utils


def test_collection_filename():
    name = "test"
    if (
        scr_collection_utils.create_collection_filename(name)
        != "export_collection_test.csv"
    ):
        raise AssertionError()


def test_get_dict_available_pages(collection_soup):
    available_pages = scr_collection_utils.get_dict_available_pages(
        collection_soup
    )
    if available_pages:
        raise AssertionError()


def test_get_next_collection_link(collection_soup):
    next_collection_link = scr_collection_utils.get_next_collection_link(
        collection_soup
    )
    if next_collection_link:
        raise AssertionError()


def test_get_rows_from_collection(collection_soup):
    rows = scr_collection_utils.get_rows_from_collection(collection_soup)
    if len(rows) != 6:
        raise AssertionError()
