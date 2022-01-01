from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_comic):
    assert survey_utils.get_category_from_survey(survey_comic) == "bd"


def test_get_rows_from_survey(survey_comic):
    rows = survey_utils.get_rows_from_survey(survey_comic)
    assert len(rows) == 10


def test_get_infos_from_survey(survey_comic):
    category = survey_utils.get_category_from_survey(survey_comic)

    infos = survey_utils.get_survey_infos(survey_comic, category)

    assert len(infos) == 10

    assert infos[0]["Title"] == "Astérix et Cléopâtre - Astérix, tome 6"
