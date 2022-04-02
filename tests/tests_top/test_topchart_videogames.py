from senscritiquescraper.utils.row_utils import row_utils


def test_videogame_rank(topchart_row_videogame):
    rank = row_utils.get_rank(topchart_row_videogame)
    assert rank == "1"


def test_videogame_title(topchart_row_videogame):
    title = row_utils.get_title(topchart_row_videogame)
    assert title == "The Legend of Zelda: Ocarina of Time"


def test_videogame_url(topchart_row_videogame):
    url = row_utils.get_url(topchart_row_videogame)
    assert url.startswith("https")


def test_videogame_original_title(topchart_row_videogame):
    original_title = row_utils.get_original_title(topchart_row_videogame)
    assert original_title == "Zelda no Densetsu: Toki no Ocarina"


def test_videogame_year(topchart_row_videogame):
    year = row_utils.get_year(topchart_row_videogame)
    assert year == "1998"


def test_videogame_release_date(topchart_row_videogame):
    release_date = row_utils.get_baseline_0(topchart_row_videogame)
    assert release_date == "11 décembre 1998 (France)"


def test_videogame_cover(topchart_row_videogame):
    cover_url = row_utils.get_picture_url(topchart_row_videogame)
    assert cover_url.startswith("https")


def test_videogame_genre(topchart_row_videogame):
    genre = row_utils.get_baseline_1(topchart_row_videogame)
    assert genre == "Action-Aventure"


def test_videogame_developer(topchart_row_videogame):
    developer = row_utils.get_producer(topchart_row_videogame)
    assert developer == "Nintendo EAD, SRD, Nintendo"


def test_videogame_platforms(topchart_row_videogame):
    platforms = row_utils.get_topchart_platforms(topchart_row_videogame)
    assert platforms == "Nintendo 64, GameCube, Wii, Wii U et Nintendo 3DS"


def test_videogame_description(topchart_row_videogame):
    description = row_utils.get_description(topchart_row_videogame)
    assert description.startswith("Un jeune garçon, Link")


def test_videogame_average_rating(topchart_row_videogame):
    average_rating = row_utils.get_average_rating(topchart_row_videogame)
    assert len(average_rating) == 3


def test_videogame_number_ratings(topchart_row_videogame):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_videogame)
    assert int(number_ratings) > 19000
