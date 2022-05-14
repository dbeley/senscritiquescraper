import logging
import difflib
from bs4 import BeautifulSoup
from typing import Optional
import urllib.parse

logger = logging.getLogger(__name__)

GENRE_CHOICES = ["Morceaux", "Albums", "Films", "Livres", "Séries", "BD", "Jeux"]


def sanitize_text(text: str) -> str:
    """Sanitize text to URL-compatible text."""
    return urllib.parse.quote_plus(text)


def get_search_url(search_term: str, genre: str = None) -> str:
    """Returns the senscritique search URL for a search term."""
    search_term_sanitized = sanitize_text(search_term)
    if genre not in GENRE_CHOICES:
        url = f"https://old.senscritique.com/search?q={search_term_sanitized}"
    else:
        url = f"https://old.senscritique.com/search?q={search_term_sanitized}&categories[0][0]={genre}"
    return url


def get_search_result(soup: BeautifulSoup, position: int) -> Optional[str]:
    """Returns the URL result of the BeautifulSoup object at the defined position."""
    try:
        url_list = [
            x.find_all("a")[1]["href"]
            for x in soup.find_all(
                "div", {"class": "ProductListItem__Container-sc-1ci68b-0"}
            )
        ]
        if position > len(url_list):
            logger.error(
                f"Desired result not found in search results (Desired result: position {position}, number of search results: {len(url_list)})."
            )
            return None
        return url_list[position - 1]
    except Exception as e:
        logger.error(e)
        return None


def get_closest_search_result(soup: BeautifulSoup, search_term: str) -> Optional[str]:
    """Returns the closest result of the results for the search_term."""
    try:
        list_candidates = []
        for url in [
            x.find_all("a")[1]["href"]
            for x in soup.find_all(
                "div", {"class": "ProductListItem__Container-sc-1ci68b-0"}
            )
        ]:
            name = url.split("/")[-2:][0].replace("_", " ") if url else None
            list_candidates.append({"url": url, "name": name})
        closest_match = difflib.get_close_matches(
            search_term, [x["name"] for x in list_candidates], 1
        )
        if closest_match:
            closest_dict = next(
                (item for item in list_candidates if item["name"] == closest_match[0]),
                None,
            )
            result = closest_dict.get("url") if closest_dict else None
        else:
            result = list_candidates[0].get("url")
        logger.info(f"{result=}")
        return result
    except Exception as e:
        raise Exception(e)
