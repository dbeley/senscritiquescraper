from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_serie):
    assert survey_utils.get_category_from_survey(survey_serie) == "series"


def test_get_rows_from_survey(survey_serie):
    rows = survey_utils.get_rows_from_survey(survey_serie)
    assert len(rows) == 75


def test_get_infos_from_survey(survey_serie):
    category = survey_utils.get_category_from_survey(survey_serie)

    infos = survey_utils.get_survey_infos(survey_serie, category)

    assert len(infos) == 75

    assert infos[0]["Title"] == "Friends"
