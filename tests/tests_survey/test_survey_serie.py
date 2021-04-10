from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_serie):
    if survey_utils.get_category_from_survey(survey_serie) != "series":
        raise AssertionError()


def test_get_rows_from_survey(survey_serie):
    rows = survey_utils.get_rows_from_survey(survey_serie)
    if len(rows) != 75:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_serie):
    category = survey_utils.get_category_from_survey(survey_serie)

    infos = survey_utils.get_survey_infos(survey_serie, category)

    if len(infos) != 75:
        raise AssertionError()

    if infos[0]["Title"] != "Friends":
        raise AssertionError()
