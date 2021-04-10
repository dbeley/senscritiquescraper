from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_comic):
    if survey_utils.get_category_from_survey(survey_comic) != "bd":
        raise AssertionError()


def test_get_rows_from_survey(survey_comic):
    rows = survey_utils.get_rows_from_survey(survey_comic)
    if len(rows) != 10:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_comic):
    category = survey_utils.get_category_from_survey(survey_comic)

    infos = survey_utils.get_survey_infos(survey_comic, category)

    if len(infos) != 10:
        raise AssertionError()

    if infos[0]["Title"] != "Astérix et Cléopâtre - Astérix, tome 6":
        raise AssertionError()
