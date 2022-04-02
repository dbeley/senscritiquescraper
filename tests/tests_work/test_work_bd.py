def test_get_work_bd(work_object_bd):
    details = work_object_bd.get_details()
    assert isinstance(details, dict)
    assert len(details) == 15


def test_rating_work_bd(work_object_bd):
    main_rating = work_object_bd.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating[0] == "5"
    assert main_rating[1] == "."
    assert len(main_rating) == 3


def test_rating_details_work_bd(work_object_bd):
    rating_details = work_object_bd.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_bd(work_object_bd):
    title = work_object_bd.get_title()
    assert title == "La Fille de Vercingétorix - Astérix, tome 38"


def test_year_work_bd(work_object_bd):
    year = work_object_bd.get_year()
    assert year == "2019"


def test_cover_url_work_bd(work_object_bd):
    cover_url = work_object_bd.get_cover_url()
    assert isinstance(cover_url, str)
    assert (
        cover_url.lower()
        == "https://media.senscritique.com/media/000018928960/160/La_Fille_de_Vercingetorix_Asterix_tome_38.jpg".lower()
    )


def test_complementary_infos_work_bd(work_object_bd):
    complementary_infos = work_object_bd.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_bd(work_object_bd):
    review_count = work_object_bd.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_bd(work_object_bd):
    vote_count = work_object_bd.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_bd(work_object_bd):
    favorite_count = work_object_bd.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_bd(work_object_bd):
    wishlist_count = work_object_bd.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_bd(work_object_bd):
    in_progress_count = work_object_bd.get_in_progress_count()
    assert isinstance(in_progress_count, str)
