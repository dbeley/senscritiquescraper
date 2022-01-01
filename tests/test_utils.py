from senscritiquescraper import Senscritique


def test_format_number():
    assert Senscritique.utils.format_number("17") == "17"
    assert Senscritique.utils.format_number("1.7K") == "1700"
    assert Senscritique.utils.format_number("127K") == "127000"
