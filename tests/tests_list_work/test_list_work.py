from senscritiquescraper.utils import list_work_utils


def test_get_rows_from_list_work(list_work_soup):
    rows = list_work_utils.get_rows_from_list_work(list_work_soup)
    assert len(rows) >= 44
