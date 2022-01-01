from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_game):
    assert survey_utils.get_category_from_survey(survey_game) == "jeuxvideo"


def test_get_rows_from_survey(survey_game):
    rows = survey_utils.get_rows_from_survey(survey_game)
    assert len(rows) == 10


def test_get_infos_from_survey(survey_game):
    category = survey_utils.get_category_from_survey(survey_game)

    infos = survey_utils.get_survey_infos(survey_game, category)

    assert len(infos) == 10

    assert infos[0]["Title"] == "Les Sims"
