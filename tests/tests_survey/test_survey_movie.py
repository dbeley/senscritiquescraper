from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_movie):
    assert survey_utils.get_category_from_survey(survey_movie) == "films"


def test_get_rows_from_survey(survey_movie):
    rows = survey_utils.get_rows_from_survey(survey_movie)
    assert len(rows) == 15


def test_get_infos_from_survey(survey_movie):
    category = survey_utils.get_category_from_survey(survey_movie)

    infos = survey_utils.get_survey_infos(survey_movie, category)

    assert len(infos) == 15

    assert infos[0]["Title"] == "La Haine"
