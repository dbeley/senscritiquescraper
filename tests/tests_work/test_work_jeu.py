def test_get_work_jeu(work_object_jeu):
    details = work_object_jeu.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 17:
        print(len(details))
        raise AssertionError()


def test_rating_work_jeu(work_object_jeu):
    main_rating = work_object_jeu.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "6.6":
        raise AssertionError()


def test_rating_details_work_jeu(work_object_jeu):
    rating_details = work_object_jeu.get_rating_details()
    if not isinstance(rating_details, dict):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_jeu(work_object_jeu):
    title = work_object_jeu.get_title()
    if not title == "Verdun":
        raise AssertionError()


def test_year_work_jeu(work_object_jeu):
    year = work_object_jeu.get_year()
    if not year == "2013":
        raise AssertionError()


def test_cover_url_work_jeu(work_object_jeu):
    cover_url = work_object_jeu.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        # == "https://media.senscritique.com/media/000009682253/160/Verdun.png"
        == "https://media.senscritique.com/media/000019964116/160/Verdun.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_jeu(work_object_jeu):
    complementary_infos = work_object_jeu.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_jeu(work_object_jeu):
    review_count = work_object_jeu.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_jeu(work_object_jeu):
    vote_count = work_object_jeu.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_jeu(work_object_jeu):
    favorite_count = work_object_jeu.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_jeu(work_object_jeu):
    wishlist_count = work_object_jeu.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_jeu(work_object_jeu):
    in_progress_count = work_object_jeu.get_in_progress_count()
    if not isinstance(in_progress_count, str):
        raise AssertionError()
