from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_book):
    assert survey_utils.get_category_from_survey(survey_book) == "livres"


def test_get_rows_from_survey(survey_book):
    rows = survey_utils.get_rows_from_survey(survey_book)
    assert len(rows) == 5


def test_get_infos_from_survey(survey_book):
    category = survey_utils.get_category_from_survey(survey_book)

    infos = survey_utils.get_survey_infos(survey_book, category)

    assert len(infos) == 5

    assert infos[0]["Title"] == "La Horde du contrevent"
