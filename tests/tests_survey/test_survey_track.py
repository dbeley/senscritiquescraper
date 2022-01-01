from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_track):
    assert survey_utils.get_category_from_survey(survey_track) == "musique"


def test_get_rows_from_survey(survey_track):
    rows = survey_utils.get_rows_from_survey(survey_track)
    assert len(rows) == 15


def test_get_infos_from_survey(survey_track):
    category = survey_utils.get_category_from_survey(survey_track)

    infos = survey_utils.get_survey_infos(survey_track, category)

    assert len(infos) == 15

    assert infos[0]["Title"] == "La Mauvaise Réputation"
