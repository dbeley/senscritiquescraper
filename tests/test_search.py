from senscritiquescraper import Senscritique


def test_search_term_simple():
    search_term = "Melancholia"
    url_search = "https://www.senscritique.com/search?q=Melancholia"
    url = "https://www.senscritique.com/film/Melancholia/411823"
    soup = Senscritique.utils.get_soup(url_search)

    if not Senscritique.search_utils.get_search_url(search_term) == url_search:
        raise AssertionError()
    if not Senscritique.search_utils.get_search_result(soup, 1) == url:
        raise AssertionError()


def test_search_term_advanced():
    search_term = "astérix, tome 17"
    url_search = "https://www.senscritique.com/search?q=ast%C3%A9rix%2C+tome+17"
    url = "https://www.senscritique.com/bd/Le_Domaine_des_dieux_Asterix_tome_17/369196"
    soup = Senscritique.utils.get_soup(url_search)

    if not Senscritique.search_utils.get_search_url(search_term) == url_search:
        raise AssertionError()
    if not Senscritique.search_utils.get_search_result(soup, 1) == url:
        raise AssertionError()


def test_search_term_advanced_2():
    search_term = "Mëkanïk Dëstruktïẁ Kömmandöh"
    url_search = "https://www.senscritique.com/search?q=M%C3%ABkan%C3%AFk+D%C3%ABstrukt%C3%AF%E1%BA%81+K%C3%B6mmand%C3%B6h"
    url = "https://www.senscritique.com/album/Mekanik_Destrukti_Koemmandoeh/5905267"
    soup = Senscritique.utils.get_soup(url_search)

    if not Senscritique.search_utils.get_search_url(search_term) == url_search:
        raise AssertionError()
    if not Senscritique.search_utils.get_search_result(soup, 1) == url:
        raise AssertionError()


def test_search_term_position():
    search_term = "XTC"
    url_search = "https://www.senscritique.com/search?q=XTC"
    url = "https://www.senscritique.com/album/Drums_and_Wires/6011492"
    soup = Senscritique.utils.get_soup(url_search)

    if not Senscritique.search_utils.get_search_url(search_term) == url_search:
        raise AssertionError()
    print(Senscritique.search_utils.get_search_result(soup, 12))
    if not Senscritique.search_utils.get_search_result(soup, 12) == url:
        raise AssertionError()


def test_search_term_genre():
    search_term = "XTC"
    genre = "Livres"
    url_search = "https://www.senscritique.com/search?q=XTC&categories[0][0]=Livres"
    url = "https://www.senscritique.com/livre/The_XTC_Bumper_Book_of_Fun_for_Boys_and_Girls/27941474"
    soup = Senscritique.utils.get_soup(url_search)

    if (
        not Senscritique.search_utils.get_search_url(search_term, genre=genre)
        == url_search
    ):
        raise AssertionError()
    if not Senscritique.search_utils.get_search_result(soup, 1) == url:
        raise AssertionError()
