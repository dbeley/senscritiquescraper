from senscritiquescraper.utils.row_utils import row_utils


def test_videogame_rank(topchart_row_videogame):
    rank = row_utils.get_rank(topchart_row_videogame)
    if rank != "1":
        raise AssertionError()


def test_videogame_title(topchart_row_videogame):
    title = row_utils.get_title(topchart_row_videogame)
    if title != "The Legend of Zelda: Ocarina of Time":
        raise AssertionError()


def test_videogame_url(topchart_row_videogame):
    url = row_utils.get_url(topchart_row_videogame)
    if not url.startswith("https"):
        raise AssertionError()


def test_videogame_original_title(topchart_row_videogame):
    original_title = row_utils.get_original_title(topchart_row_videogame)
    if original_title != "Zelda no Densetsu : Toki no Ocarina":
        raise AssertionError()


def test_videogame_year(topchart_row_videogame):
    year = row_utils.get_year(topchart_row_videogame)
    if year != "1998":
        raise AssertionError()


def test_videogame_release_date(topchart_row_videogame):
    release_date = row_utils.get_baseline_0(topchart_row_videogame)
    if release_date != "Sortie : 11 décembre 1998":
        raise AssertionError()


def test_videogame_cover(topchart_row_videogame):
    cover_url = row_utils.get_picture_url(topchart_row_videogame)
    if not cover_url.startswith("https"):
        raise AssertionError()


def test_videogame_genre(topchart_row_videogame):
    genre = row_utils.get_baseline_1(topchart_row_videogame)
    if genre != "Action-Aventure":
        raise AssertionError()


def test_videogame_developer(topchart_row_videogame):
    developer = row_utils.get_producer(topchart_row_videogame)
    if developer != "Nintendo EAD, Nintendo":
        raise AssertionError()


def test_videogame_platforms(topchart_row_videogame):
    platforms = row_utils.get_platforms(topchart_row_videogame)
    if platforms != "Nintendo 64, GameCube, Wii, Wii U et Nintendo 3DS":
        raise AssertionError()


def test_videogame_description(topchart_row_videogame):
    description = row_utils.get_description(topchart_row_videogame)
    if not description.startswith("Un jeune garçon, Link"):
        raise AssertionError()


def test_videogame_average_rating(topchart_row_videogame):
    average_rating = row_utils.get_average_rating(topchart_row_videogame)
    if len(average_rating) != 3:
        raise AssertionError()


def test_videogame_number_ratings(topchart_row_videogame):
    number_ratings = row_utils.get_number_of_ratings(topchart_row_videogame)
    if not int(number_ratings) > 19000:
        raise AssertionError()
