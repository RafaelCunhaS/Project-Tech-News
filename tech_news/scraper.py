from time import sleep
from parsel import Selector
import requests
# from tech_news.database import create_news


def fetch(url):
    try:
        headers = {"user-agent": "Fake user-agent"}
        response = requests.get(url, timeout=3, headers=headers)
        response.raise_for_status()
        sleep(1)
        return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


def scrape_novidades(html_content):
    selector = Selector(html_content)
    news = selector.css("h2.entry-title a::attr(href)").getall()
    return news


def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    return next_page


def scrape_noticia(html_content):
    pass


def get_tech_news(amount):
    pass
