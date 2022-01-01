def test_get_work_livre(work_object_livre):
    details = work_object_livre.get_details()
    assert isinstance(details, dict)
    assert len(details) == 16


def test_rating_work_livre(work_object_livre):
    main_rating = work_object_livre.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating == "5.9"


def test_rating_details_work_livre(work_object_livre):
    rating_details = work_object_livre.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_livre(work_object_livre):
    title = work_object_livre.get_title()
    assert title == "Soif"


def test_year_work_livre(work_object_livre):
    year = work_object_livre.get_year()
    assert year == "2019"


def test_cover_url_work_livre(work_object_livre):
    cover_url = work_object_livre.get_cover_url()
    assert isinstance(cover_url, str)
    assert cover_url == "https://media.senscritique.com/media/000018573228/160/Soif.jpg"


def test_complementary_infos_work_livre(work_object_livre):
    complementary_infos = work_object_livre.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_livre(work_object_livre):
    review_count = work_object_livre.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_livre(work_object_livre):
    vote_count = work_object_livre.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_livre(work_object_livre):
    favorite_count = work_object_livre.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_livre(work_object_livre):
    wishlist_count = work_object_livre.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_livre(work_object_livre):
    in_progress_count = work_object_livre.get_in_progress_count()
    assert isinstance(in_progress_count, str)
