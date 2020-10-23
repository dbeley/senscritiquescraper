def test_get_work_livre(work_object_livre):
    details = work_object_livre.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 15:
        print(len(details))
        raise AssertionError()


def test_rating_work_livre(work_object_livre):
    main_rating = work_object_livre.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "5.9":
        raise AssertionError()


def test_rating_details_work_livre(work_object_livre):
    rating_details = work_object_livre.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_livre(work_object_livre):
    title = work_object_livre.get_title()
    if not title == "Soif":
        raise AssertionError()


def test_year_work_livre(work_object_livre):
    year = work_object_livre.get_year()
    if not year == "2019":
        raise AssertionError()


def test_cover_url_work_livre(work_object_livre):
    cover_url = work_object_livre.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000018573228/160/Soif.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_livre(work_object_livre):
    complementary_infos = work_object_livre.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_livre(work_object_livre):
    review_count = work_object_livre.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_livre(work_object_livre):
    vote_count = work_object_livre.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_livre(work_object_livre):
    favorite_count = work_object_livre.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_livre(work_object_livre):
    wishlist_count = work_object_livre.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_livre(work_object_livre):
    in_progress_count = work_object_livre.get_in_progress_count()
    if not isinstance(in_progress_count, str):
        raise AssertionError()
