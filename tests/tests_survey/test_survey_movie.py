from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_movie):
    if survey_utils.get_category_from_survey(survey_movie) != "films":
        raise AssertionError()


def test_get_rows_from_survey(survey_movie):
    rows = survey_utils.get_rows_from_survey(survey_movie)
    if len(rows) != 15:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_movie):
    category = survey_utils.get_category_from_survey(survey_movie)

    infos = survey_utils.get_survey_infos(survey_movie, category)

    if len(infos) != 15:
        raise AssertionError()

    if infos[0]["Title"] != "La Haine":
        raise AssertionError()
