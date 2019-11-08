def test_get_work_film(work_object_film):
    details = work_object_film.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 16:
        print(len(details))
        raise AssertionError()


def test_rating_work_film(work_object_film):
    main_rating = work_object_film.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "7.4":
        raise AssertionError()


def test_rating_details_work_film(work_object_film):
    rating_details = work_object_film.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_film(work_object_film):
    title = work_object_film.get_title()
    if not title == "Le Chant du loup":
        raise AssertionError()


def test_year_work_film(work_object_film):
    year = work_object_film.get_year()
    if not year == "2019":
        raise AssertionError()


def test_cover_url_work_film(work_object_film):
    cover_url = work_object_film.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000018537250/160/Le_Chant_du_loup.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_film(work_object_film):
    complementary_infos = work_object_film.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_film(work_object_film):
    review_count = work_object_film.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_film(work_object_film):
    vote_count = work_object_film.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_film(work_object_film):
    favorite_count = work_object_film.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_film(work_object_film):
    wishlist_count = work_object_film.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_film(work_object_film):
    in_progress_count = work_object_film.get_in_progress_count()
    if in_progress_count:
        raise AssertionError()
