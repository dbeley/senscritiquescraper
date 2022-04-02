def test_get_work_serie(work_object_serie):
    details = work_object_serie.get_details()
    assert isinstance(details, dict)
    assert len(details) == 19


def test_rating_work_serie(work_object_serie):
    main_rating = work_object_serie.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating == "7.8"


def test_rating_details_work_serie(work_object_serie):
    rating_details = work_object_serie.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_serie(work_object_serie):
    title = work_object_serie.get_title()
    assert title == "The Handmaid's Tale : La Servante écarlate"


def test_year_work_serie(work_object_serie):
    year = work_object_serie.get_year()
    assert year == "2017"


def test_cover_url_work_serie(work_object_serie):
    cover_url = work_object_serie.get_cover_url()
    assert isinstance(cover_url, str)
    assert (
        cover_url.lower()
        == "https://media.senscritique.com/media/000016972804/160/The_Handmaid_s_Tale_La_Servante_ecarlate.jpg".lower()
    )


def test_complementary_infos_work_serie(work_object_serie):
    complementary_infos = work_object_serie.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_serie(work_object_serie):
    review_count = work_object_serie.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_serie(work_object_serie):
    vote_count = work_object_serie.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_serie(work_object_serie):
    favorite_count = work_object_serie.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_serie(work_object_serie):
    wishlist_count = work_object_serie.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_serie(work_object_serie):
    in_progress_count = work_object_serie.get_in_progress_count()
    assert isinstance(in_progress_count, str)
