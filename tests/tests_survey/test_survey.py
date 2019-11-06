from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_soup):
    if survey_utils.get_category_from_survey(survey_soup) != "films":
        raise AssertionError()


def test_get_rows_from_survey(survey_soup):
    rows = survey_utils.get_rows_from_survey(survey_soup)
    if len(rows) != 15:
        raise AssertionError()
