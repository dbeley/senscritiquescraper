from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_track):
    if survey_utils.get_category_from_survey(survey_track) != "musique":
        raise AssertionError()


def test_get_rows_from_survey(survey_track):
    rows = survey_utils.get_rows_from_survey(survey_track)
    if len(rows) != 15:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_track):
    category = survey_utils.get_category_from_survey(survey_track)

    infos = survey_utils.get_survey_infos(survey_track, category)

    if len(infos) != 15:
        raise AssertionError()

    if infos[0]["Title"] != "La mauvaise reputation":
        raise AssertionError()
