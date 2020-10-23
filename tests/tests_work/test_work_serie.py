def test_get_work_serie(work_object_serie):
    details = work_object_serie.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 18:
        print(len(details))
        raise AssertionError()


def test_rating_work_serie(work_object_serie):
    main_rating = work_object_serie.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "7.9":
        raise AssertionError()


def test_rating_details_work_serie(work_object_serie):
    rating_details = work_object_serie.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_serie(work_object_serie):
    title = work_object_serie.get_title()
    if not title == "The Handmaid's Tale : La Servante écarlate":
        raise AssertionError()


def test_year_work_serie(work_object_serie):
    year = work_object_serie.get_year()
    if not year == "2017":
        raise AssertionError()


def test_cover_url_work_serie(work_object_serie):
    cover_url = work_object_serie.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000016972804/160/The_Handmaid_s_Tale_La_Servante_ecarlate.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_serie(work_object_serie):
    complementary_infos = work_object_serie.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_serie(work_object_serie):
    review_count = work_object_serie.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_serie(work_object_serie):
    vote_count = work_object_serie.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_serie(work_object_serie):
    favorite_count = work_object_serie.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_serie(work_object_serie):
    wishlist_count = work_object_serie.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_serie(work_object_serie):
    in_progress_count = work_object_serie.get_in_progress_count()
    if not isinstance(in_progress_count, str):
        raise AssertionError()
