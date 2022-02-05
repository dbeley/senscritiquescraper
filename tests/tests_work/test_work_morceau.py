def test_get_work_morceau(work_object_morceau):
    details = work_object_morceau.get_details()
    assert isinstance(details, dict)
    assert len(details) == 16


def test_rating_work_morceau(work_object_morceau):
    main_rating = work_object_morceau.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating == "7.6"


def test_rating_details_work_morceau(work_object_morceau):
    rating_details = work_object_morceau.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_morceau(work_object_morceau):
    title = work_object_morceau.get_title()
    assert title == "Les Copains d’abord"


def test_year_work_morceau(work_object_morceau):
    year = work_object_morceau.get_year()
    assert year == "1991"


def test_cover_url_work_morceau(work_object_morceau):
    cover_url = work_object_morceau.get_cover_url()
    assert isinstance(cover_url, str)
    assert (
        cover_url
        == "https://media.senscritique.com/media/000000194665/160/les_copains_dabord.jpg"
    )


def test_complementary_infos_work_morceau(work_object_morceau):
    complementary_infos = work_object_morceau.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_morceau(work_object_morceau):
    review_count = work_object_morceau.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_morceau(work_object_morceau):
    vote_count = work_object_morceau.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_morceau(work_object_morceau):
    favorite_count = work_object_morceau.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_morceau(work_object_morceau):
    wishlist_count = work_object_morceau.get_wishlist_count()
    assert isinstance(wishlist_count, str)
