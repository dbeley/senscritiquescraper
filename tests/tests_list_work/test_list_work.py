from senscritiquescraper.utils import list_work_utils


def test_get_category_from_list_work(list_work_soup):
    if list_work_utils.get_category_from_survey(list_work_soup) != "series":
        raise AssertionError()


def test_get_rows_from_list_work(list_work_soup):
    rows = list_work_utils.get_rows_from_survey(list_work_soup)
    if len(rows) != 15:
        raise AssertionError()
