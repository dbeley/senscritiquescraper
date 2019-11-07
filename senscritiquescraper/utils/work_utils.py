import logging
from typing import List, Dict
from bs4 import BeautifulSoup, element
from . import utils


logger = logging.getLogger(__name__)


class Work:
    def __init__(self, url):
        self.url = url

    def export(self):
        return {
            "title": self.title,
            "url": self.url,
            "main_rating": self.main_rating,
            "rating_details": self.rating_details,
            "release_date": self.release_date,
            "cover_url": self.cover_url,
            "complementary_infos": self.complementary_infos,
            "review_number": self.review_number,
        }

    def get_work_details(self):
        self.soup = utils.get_soup(self.url)
        self.main_rating = self.get_main_rating()
        self.rating_details = self.get_rating_details()
        self.title = self.get_title()
        self.release_date = self.get_release_date()
        self.cover_url = self.get_cover_url()
        self.review_number = self.get_review_number()
        self.complementary_infos = self.get_complementary_infos()
        return self.export()

    def get_main_rating(self) -> str:
        try:
            return self.soup.find("span", {"class": "pvi-scrating-value"}).text
        except Exception as e:
            logger.error(e)
            return None

    def get_rating_details(self) -> List:
        try:
            rating_details = [
                i.find("div").text
                for i in self.soup.find(
                    "div", {"class": "pvi-scrating-graph"}
                ).find_all("li", {"class": "elrg-graph-col"})
            ]
            return rating_details[0:10]
        except Exception as e:
            logger.error(e)
            return None

    def get_title(self) -> str:
        try:
            return self.soup.find(
                "h1", {"class": "pvi-product-title"}
            ).text.strip()
        except Exception as e:
            logger.error(e)
            return None

    def get_release_date(self) -> str:
        try:
            return (
                self.soup.find("small", {"class": "pvi-product-year"})
                .text.replace("(", "")
                .replace(")", "")
            )
        except Exception as e:
            logger.error(e)
            return None

    def get_cover_url(self) -> str:
        try:
            return self.soup.find("img", {"class": "pvi-hero-poster"})["href"]
        except Exception as e:
            logger.error(e)
            return None

    def get_review_number(self) -> str:
        try:
            return self.soup.find("h5", {"class": "d-heading2-opt"}).text
        except Exception as e:
            logger.error(e)
            return None

    def get_complementary_infos(self) -> Dict:
        try:
            return [
                i.find("li").text
                for i in self.soup.find(
                    "section", {"class": "pvi-productDetails"}
                )
            ]
        except Exception as e:
            logger.error(e)
            return None
