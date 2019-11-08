from senscritiquescraper import Senscritique


def test_format_number():
    if not Senscritique.utils.format_number("17") == "17":
        raise AssertionError()
    if not Senscritique.utils.format_number("1.7K") == "1700":
        raise AssertionError()
    if not Senscritique.utils.format_number("127K") == "127000":
        raise AssertionError()
