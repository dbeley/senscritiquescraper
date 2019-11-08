import logging
from typing import List, Dict
from . import utils


logger = logging.getLogger(__name__)


class Work:
    def __init__(self, url):
        self.url = url
        self.category = self.get_category()

    def export(self):
        return {
            **{
                "Title": self.title,
                "URL": self.url,
                "Rating": self.main_rating,
                "Rating Details": self.rating_details,
                "Year": self.year,
                "Cover URL": self.cover_url,
                "Review Count": self.review_count,
                "Vote Count": self.vote_count,
                "Favorite Count": self.favorite_count,
                "Wishlist Count": self.wishlist_count,
                "In Progress Count": self.in_progress_count,
            },
            **self.get_complementary_infos(),
            **{"Category": self.category},
        }

    def get_category(self):
        category = self.url.split("/")[3]
        if category == "film":
            return "Movie"
        elif category == "serie":
            return "Series"
        elif category == "jeuvideo":
            return "Video Game"
        elif category == "livre":
            return "Book"
        elif category == "bd":
            return "Comics"
        elif category == "album":
            return "Music"

    def get_details(self):
        self.soup = utils.get_soup(self.url)
        self.main_rating = self.get_main_rating()
        self.rating_details = self.get_rating_details()
        self.vote_count = self.get_vote_count()
        self.favorite_count = self.get_favorite_count()
        self.wishlist_count = self.get_wishlist_count()
        self.in_progress_count = self.get_in_progress_count()
        self.title = self.get_title()
        self.year = self.get_year()
        self.cover_url = self.get_cover_url()
        self.review_count = self.get_review_count()
        # self.complementary_infos = self.get_complementary_infos()
        return self.export()

    def get_main_rating(self) -> str:
        try:
            return self.soup.find("span", {"class": "pvi-scrating-value"}).text
        except Exception as e:
            logger.error("Function get_main_rating : %s.", e)
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
            logger.error("Function get_rating_details : %s.", e)
            return None

    def get_vote_count(self):
        try:
            return self.soup.find("meta", {"itemprop": "ratingCount"})[
                "content"
            ]
        except Exception as e:
            logger.error("Function get_vote_count : %s.", e)
            return None

    def get_favorite_count(self):
        try:
            favorite_count = (
                self.soup.find("li", {"title": "Coups de coeur"})
                .find("b")
                .text
            )
            return utils.format_number(favorite_count)
        except Exception as e:
            logger.error("Function get_favorite_count : %s.", e)
            return None

    def get_wishlist_count(self):
        try:
            wishlist_count = (
                self.soup.find("li", {"title": "Envies"}).find("b").text
            )
            return utils.format_number(wishlist_count)
        except Exception as e:
            logger.error("Function get_wishlist_count : %s.", e)
            return None

    def get_in_progress_count(self):
        try:
            in_progress_count = (
                self.soup.find("li", {"title": "En cours"}).find("b").text
            )
            return utils.format_number(in_progress_count)
        except Exception as e:
            logger.error("Function get_in_progress_count : %s.", e)
            return None

    def get_title(self) -> str:
        try:
            return self.soup.find(
                "h1", {"class": "pvi-product-title"}
            ).text.strip()
        except Exception as e:
            logger.error("Function get_title : %s.", e)
            return None

    def get_year(self) -> str:
        try:
            return (
                self.soup.find("small", {"class": "pvi-product-year"})
                .text.replace("(", "")
                .replace(")", "")
            )
        except Exception as e:
            logger.error("Function get_year : %s.", e)
            return None

    def get_cover_url(self) -> str:
        try:
            return self.soup.find("img", {"class": "pvi-hero-poster"})["src"]
        except Exception as e:
            logger.error("Function get_cover_url : %s.", e)
            return None

    def get_review_count(self) -> str:
        try:
            return self.soup.find("meta", {"itemprop": "reviewCount"})[
                "content"
            ]
        except Exception as e:
            logger.error("Function get_review_count : %s.", e)
            return None

    def get_complementary_infos(self) -> Dict:
        try:
            complementary_infos = [
                i.text.replace("\n", "").replace("\t", "").strip()
                for i in self.soup.find(
                    "section", {"class": "pvi-productDetails"}
                ).find_all("li")
            ]
            if self.category == "Movie":
                return {
                    "Producer": complementary_infos[0],
                    "Genre": complementary_infos[1],
                    "Length": complementary_infos[2],
                    "Release Date": complementary_infos[3],
                }
            if self.category == "Series":
                return {
                    "Producer": complementary_infos[0],
                    "Genre": complementary_infos[1],
                    "Season Number": complementary_infos[2],
                    "Editor": complementary_infos[3],
                    "Episode Length": complementary_infos[4],
                    "Release Date": complementary_infos[5],
                }
            if self.category == "Video Game":
                return {
                    "Developer": complementary_infos[0],
                    "Platforms": complementary_infos[1],
                    "Genre": complementary_infos[2],
                    "Release Date": complementary_infos[3],
                }
            if self.category == "Book":
                return {
                    "Writer": complementary_infos[0],
                    "Genre": complementary_infos[1],
                    "Release Date": complementary_infos[2],
                }
            if self.category == "Comics":
                return {
                    "Writer": complementary_infos[0],
                    "Release Date": complementary_infos[1],
                }
            if self.category == "Music":
                return {
                    "Artist": complementary_infos[0],
                    "Genre": complementary_infos[1],
                    "Label": complementary_infos[2],
                    "Release Date": complementary_infos[3],
                }
        except Exception as e:
            logger.error("Function get_complementary_infos : %s.", e)
            return None
