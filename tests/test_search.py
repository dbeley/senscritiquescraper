import pytest
from senscritiquescraper import Senscritique


def test_search_term_simple():
    search_term = "Melancholia"
    url_search = (
        "https://old.senscritique.com/search?q=Melancholia&categories[0][0]=Films"
    )
    url = "https://www.senscritique.com/film/melancholia/411823"
    soup = Senscritique.utils.get_soup(url_search)

    assert Senscritique.search_utils.get_search_url(search_term, "Films") == url_search
    assert Senscritique.search_utils.get_search_result(soup, 1).lower() == url.lower()


def test_search_term_advanced():
    search_term = "le domaine des dieux astérix, tome 17"
    url_search = "https://old.senscritique.com/search?q=le+domaine+des+dieux+ast%C3%A9rix%2C+tome+17"
    url = "https://www.senscritique.com/bd/le_domaine_des_dieux_asterix_tome_17/369196"
    soup = Senscritique.utils.get_soup(url_search)

    assert Senscritique.search_utils.get_search_url(search_term) == url_search
    assert Senscritique.search_utils.get_search_result(soup, 1) == url
    assert Senscritique.search_utils.get_closest_search_result(soup, search_term) == url


def test_search_term_advanced_2():
    search_term = "Mëkanïk Dëstruktïẁ Kömmandöh"
    url_search = "https://old.senscritique.com/search?q=M%C3%ABkan%C3%AFk+D%C3%ABstrukt%C3%AF%E1%BA%81+K%C3%B6mmand%C3%B6h&categories[0][0]=Albums"
    url = "https://www.senscritique.com/album/mekanik_destruktiw_kommandoh/5905267"
    soup = Senscritique.utils.get_soup(url_search)

    assert Senscritique.search_utils.get_search_url(search_term, "Albums") == url_search
    assert Senscritique.search_utils.get_search_result(soup, 1) == url
    assert Senscritique.search_utils.get_closest_search_result(soup, search_term) == url


def test_search_term_position():
    search_term = "XTC"
    url_search = "https://old.senscritique.com/search?q=XTC"
    url = "https://www.senscritique.com/album/drums_and_wires/6011492"
    url_2 = "https://www.senscritique.com/morceau/making_plans_for_nigel/286090"
    soup = Senscritique.utils.get_soup(url_search)

    assert Senscritique.search_utils.get_search_url(search_term) == url_search
    assert (
        Senscritique.search_utils.get_closest_search_result(soup, "Drums and Wires")
        == url
    )
    assert Senscritique.search_utils.get_search_result(soup, 12) == url_2


def test_search_term_genre():
    search_term = "XTC"
    genre = "Livres"
    url_search = "https://old.senscritique.com/search?q=XTC&categories[0][0]=Livres"
    url = "https://www.senscritique.com/livre/The_XTC_Bumper_Book_of_Fun_for_Boys_and_Girls/27941474"
    soup = Senscritique.utils.get_soup(url_search)

    assert (
        Senscritique.search_utils.get_search_url(search_term, genre=genre) == url_search
    )
    assert Senscritique.search_utils.get_search_result(soup, 1) == url
    # Exception raised because no closest match where found
    assert Senscritique.search_utils.get_closest_search_result(soup, search_term) == url
