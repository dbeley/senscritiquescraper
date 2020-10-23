def test_get_work_album(work_object_album):
    details = work_object_album.get_details()
    if not isinstance(details, dict):
        raise AssertionError()

    if not len(details) == 16:
        print(len(details))
        raise AssertionError()


def test_rating_work_album(work_object_album):
    main_rating = work_object_album.get_main_rating()
    if not isinstance(main_rating, str):
        raise AssertionError()

    if not main_rating == "7.5":
        raise AssertionError()


def test_rating_details_work_album(work_object_album):
    rating_details = work_object_album.get_rating_details()
    if not isinstance(rating_details, list):
        raise AssertionError()

    if not len(rating_details) == 10:
        raise AssertionError()


def test_title_work_album(work_object_album):
    title = work_object_album.get_title()
    if not title == "Spiritual Instinct":
        raise AssertionError()


def test_year_work_album(work_object_album):
    year = work_object_album.get_year()
    if not year == "2019":
        raise AssertionError()


def test_cover_url_work_album(work_object_album):
    cover_url = work_object_album.get_cover_url()
    if not isinstance(cover_url, str):
        raise AssertionError()

    if (
        not cover_url
        == "https://media.senscritique.com/media/000018720065/160/Spiritual_Instinct.jpg"
    ):
        raise AssertionError()


def test_complementary_infos_work_album(work_object_album):
    complementary_infos = work_object_album.get_complementary_infos()
    if not isinstance(complementary_infos, dict):
        raise AssertionError()


def test_review_count_work_album(work_object_album):
    review_count = work_object_album.get_review_count()
    if not isinstance(review_count, str):
        raise AssertionError()


def test_vote_count_work_album(work_object_album):
    vote_count = work_object_album.get_vote_count()
    if not isinstance(vote_count, str):
        raise AssertionError()


def test_favorite_count_work_album(work_object_album):
    favorite_count = work_object_album.get_favorite_count()
    if not isinstance(favorite_count, str):
        raise AssertionError()


def test_wishlist_count_work_album(work_object_album):
    wishlist_count = work_object_album.get_wishlist_count()
    if not isinstance(wishlist_count, str):
        raise AssertionError()


def test_in_progress_count_work_album(work_object_album):
    in_progress_count = work_object_album.get_in_progress_count()
    if not isinstance(in_progress_count, str):
        raise AssertionError()
