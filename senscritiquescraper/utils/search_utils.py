import logging
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
        url = f"https://www.senscritique.com/search?q={search_term_sanitized}"
    else:
        url = f"https://www.senscritique.com/search?q={search_term_sanitized}&categories[0][0]={genre}"
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
