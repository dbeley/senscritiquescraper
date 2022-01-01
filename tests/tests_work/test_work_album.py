def test_get_work_album(work_object_album):
    details = work_object_album.get_details()
    assert isinstance(details, dict)
    assert len(details) == 17


def test_rating_work_album(work_object_album):
    main_rating = work_object_album.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating == "7.6"


def test_rating_details_work_album(work_object_album):
    rating_details = work_object_album.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_album(work_object_album):
    title = work_object_album.get_title()
    assert title == "Spiritual Instinct"


def test_year_work_album(work_object_album):
    year = work_object_album.get_year()
    assert year == "2019"


def test_cover_url_work_album(work_object_album):
    cover_url = work_object_album.get_cover_url()
    assert isinstance(cover_url, str)

    assert (
        cover_url
        == "https://media.senscritique.com/media/000018720065/160/Spiritual_Instinct.jpg"
    )


def test_complementary_infos_work_album(work_object_album):
    complementary_infos = work_object_album.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_album(work_object_album):
    review_count = work_object_album.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_album(work_object_album):
    vote_count = work_object_album.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_album(work_object_album):
    favorite_count = work_object_album.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_album(work_object_album):
    wishlist_count = work_object_album.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_album(work_object_album):
    in_progress_count = work_object_album.get_in_progress_count()
    assert isinstance(in_progress_count, str)
