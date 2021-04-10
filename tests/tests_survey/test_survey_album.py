from senscritiquescraper.utils import survey_utils


def test_get_category_from_survey(survey_album):
    if survey_utils.get_category_from_survey(survey_album) != "musique":
        raise AssertionError()


def test_get_rows_from_survey(survey_album):
    rows = survey_utils.get_rows_from_survey(survey_album)
    if len(rows) != 10:
        print(len(rows))
        raise AssertionError()


def test_get_infos_from_survey(survey_album):
    category = survey_utils.get_category_from_survey(survey_album)

    infos = survey_utils.get_survey_infos(survey_album, category)

    if len(infos) != 10:
        raise AssertionError()

    if infos[0]["Title"] != "Initials B.B.":
        raise AssertionError()
