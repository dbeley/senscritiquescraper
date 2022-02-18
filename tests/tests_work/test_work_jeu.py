def test_get_work_jeu(work_object_jeu):
    details = work_object_jeu.get_details()
    assert isinstance(details, dict)
    assert len(details) == 17


def test_rating_work_jeu(work_object_jeu):
    main_rating = work_object_jeu.get_main_rating()
    assert isinstance(main_rating, str)
    assert main_rating[0] == "6"
    assert main_rating[1] == "."


def test_rating_details_work_jeu(work_object_jeu):
    rating_details = work_object_jeu.get_rating_details()
    assert isinstance(rating_details, dict)
    assert len(rating_details) == 10


def test_title_work_jeu(work_object_jeu):
    title = work_object_jeu.get_title()
    assert title == "Verdun"


def test_year_work_jeu(work_object_jeu):
    year = work_object_jeu.get_year()
    assert year == "2013"


def test_cover_url_work_jeu(work_object_jeu):
    cover_url = work_object_jeu.get_cover_url()
    assert isinstance(cover_url, str)
    assert (
        cover_url == "https://media.senscritique.com/media/000019964116/160/Verdun.jpg"
    )


def test_complementary_infos_work_jeu(work_object_jeu):
    complementary_infos = work_object_jeu.get_complementary_infos()
    assert isinstance(complementary_infos, dict)


def test_review_count_work_jeu(work_object_jeu):
    review_count = work_object_jeu.get_review_count()
    assert isinstance(review_count, str)


def test_vote_count_work_jeu(work_object_jeu):
    vote_count = work_object_jeu.get_vote_count()
    assert isinstance(vote_count, str)


def test_favorite_count_work_jeu(work_object_jeu):
    favorite_count = work_object_jeu.get_favorite_count()
    assert isinstance(favorite_count, str)


def test_wishlist_count_work_jeu(work_object_jeu):
    wishlist_count = work_object_jeu.get_wishlist_count()
    assert isinstance(wishlist_count, str)


def test_in_progress_count_work_jeu(work_object_jeu):
    in_progress_count = work_object_jeu.get_in_progress_count()
    assert isinstance(in_progress_count, str)
