def test_get_work_morceau(work_object_morceau):
    details = work_object_morceau.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 16:
        print(len(details))
        raise AssertionError()


def test_rating_work_morceau(work_object_morceau):
    main_rating = work_object_morceau.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "7.6":
        raise AssertionError()


def test_rating_details_work_morceau(work_object_morceau):
    rating_details = work_object_morceau.get_rating_details()
    if not isinstance(rating_details, dict):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_morceau(work_object_morceau):
    title = work_object_morceau.get_title()
    if not title == "Les Copains d'abord":
        raise AssertionError()


def test_year_work_morceau(work_object_morceau):
    year = work_object_morceau.get_year()
    if not year == "1991":
        raise AssertionError()


def test_cover_url_work_morceau(work_object_morceau):
    cover_url = work_object_morceau.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000000194665/160/Les_Copains_d_abord.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_morceau(work_object_morceau):
    complementary_infos = work_object_morceau.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_morceau(work_object_morceau):
    review_count = work_object_morceau.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_morceau(work_object_morceau):
    vote_count = work_object_morceau.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_morceau(work_object_morceau):
    favorite_count = work_object_morceau.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_morceau(work_object_morceau):
    wishlist_count = work_object_morceau.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


# def test_in_progress_count_work_morceau(work_object_morceau):
#     # individual tracks don't have in_progress element
#     in_progress_count = work_object_morceau.get_in_progress_count()
#     if in_progress_count:
#         raise AssertionError()
