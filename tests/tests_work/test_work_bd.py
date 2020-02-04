def test_get_work_bd(work_object_bd):
    details = work_object_bd.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 14:
        print(len(details))
        raise AssertionError()


def test_rating_work_bd(work_object_bd):
    main_rating = work_object_bd.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "5.7":
        raise AssertionError()


def test_rating_details_work_bd(work_object_bd):
    rating_details = work_object_bd.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_bd(work_object_bd):
    title = work_object_bd.get_title()
    if not title == "La Fille de Vercingétorix - Astérix, tome 38":
        raise AssertionError()


def test_year_work_bd(work_object_bd):
    year = work_object_bd.get_year()
    if not year == "2019":
        raise AssertionError()


def test_cover_url_work_bd(work_object_bd):
    cover_url = work_object_bd.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000018928960/160/La_Fille_de_Vercingetorix_Asterix_tome_38.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_bd(work_object_bd):
    complementary_infos = work_object_bd.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_bd(work_object_bd):
    review_count = work_object_bd.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_bd(work_object_bd):
    vote_count = work_object_bd.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_bd(work_object_bd):
    favorite_count = work_object_bd.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_bd(work_object_bd):
    wishlist_count = work_object_bd.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_bd(work_object_bd):
    in_progress_count = work_object_bd.get_in_progress_count()
    if not isinstance(in_progress_count, str):
        raise AssertionError()
