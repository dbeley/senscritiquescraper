from senscritiquescraper.utils import work_utils


def test_get_work(work_object):
    details = work_object.get_work_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 8:
        raise AssertionError()


def test_get_main_rating(work_object):
    main_rating = work_object.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "7.4":
        raise AssertionError()


def test_get_rating_details(work_object):
    rating_details = work_object.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_get_title(work_object):
    title = work_object.get_title()
    if not title == "Le Chant du loup":
        raise AssertionError()


def test_get_release_date(work_object):
    release_date = work_object.get_release_date()
    if not release_date == "2019":
        raise AssertionError()


def test_get_cover_url(work_object):
    cover_url = work_object.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000018537250/160/Le_Chant_du_loup.jpg"
    ):
        raise AssertionError()


def test_get_complementary_infos(work_object):
    complementary_infos = work_object.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_get_review_number(work_object):
    review_number = work_object.get_review_number()
    if not isinstance(review_number, str):
        raise AssertionError()
