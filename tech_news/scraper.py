from time import sleep
from parsel import Selector
import requests
from tech_news.database import create_news


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
    selector = Selector(html_content)
    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": (selector.css("h1.entry-title::text").get()).strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("span.author a::text").get(),
        "comments_count": selector.css("span.author a::text").re_first(r"\d")
        if None
        else 0,
        "summary": "".join(
            selector.xpath(
                "string(//div[@class='entry-content']//p[1])"
            ).getall()
        ).strip(),
        "tags": selector.css("section.post-tags li a::text").getall(),
        "category": selector.css("div.entry-details span.label::text").get(),
    }


def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []
    n = 0

    while n < amount:
        html_content = fetch(url)
        for new in scrape_novidades(html_content):
            if n == amount:
                break
            new_details = fetch(new)
            news.append(scrape_noticia(new_details))
            n += 1
        url = scrape_next_page_link(html_content)

    create_news(news)

    return news
