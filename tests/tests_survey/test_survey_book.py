from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_book):
    if survey_utils.get_category_from_survey(survey_book) != "livres":
        raise AssertionError()


def test_get_rows_from_survey(survey_book):
    rows = survey_utils.get_rows_from_survey(survey_book)
    if len(rows) != 5:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_book):
    category = survey_utils.get_category_from_survey(survey_book)

    infos = survey_utils.get_survey_infos(survey_book, category)

    if len(infos) != 5:
        raise AssertionError()

    if infos[0]["Title"] != "La Horde du contrevent":
        raise AssertionError()
