def test_get_work_film(work_object_film):
    details = work_object_film.get_details()
    assert isinstance(details, dict)
    assert len(details) == 17


def test_rating_work_film(work_object_film):
    main_rating = work_object_film.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating == "7.3"


def test_rating_details_work_film(work_object_film):
    rating_details = work_object_film.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_film(work_object_film):
    title = work_object_film.get_title()
    assert title == "Le Chant du loup"


def test_year_work_film(work_object_film):
    year = work_object_film.get_year()
    assert year == "2019"


def test_cover_url_work_film(work_object_film):
    cover_url = work_object_film.get_cover_url()
    assert isinstance(cover_url, str)

    assert (
        cover_url
        == "https://media.senscritique.com/media/000018537250/160/Le_Chant_du_loup.jpg"
    )


def test_complementary_infos_work_film(work_object_film):
    complementary_infos = work_object_film.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_film(work_object_film):
    review_count = work_object_film.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_film(work_object_film):
    vote_count = work_object_film.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_film(work_object_film):
    favorite_count = work_object_film.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_film(work_object_film):
    wishlist_count = work_object_film.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_film(work_object_film):
    # movies don't have in_progress element
    in_progress_count = work_object_film.get_in_progress_count()
    assert not in_progress_count
