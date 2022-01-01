from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_album):
    assert survey_utils.get_category_from_survey(survey_album) == "musique"


def test_get_rows_from_survey(survey_album):
    rows = survey_utils.get_rows_from_survey(survey_album)
    assert len(rows) == 10


def test_get_infos_from_survey(survey_album):
    category = survey_utils.get_category_from_survey(survey_album)

    infos = survey_utils.get_survey_infos(survey_album, category)

    assert len(infos) == 10

    assert infos[0]["Title"] == "Initials B.B."
