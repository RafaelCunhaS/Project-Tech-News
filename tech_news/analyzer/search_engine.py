from tech_news.database import search_news
from datetime import date as d


def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]


def search_by_date(date):
    try:
        news = search_news(
            {"timestamp": d.fromisoformat(date).strftime("%d/%m/%Y")}
        )
        return [
            (new["title"], new["url"])
            for new in news
        ]
    except ValueError:
        raise ValueError("Data inválida")


def search_by_tag(tag):
    news = search_news({"tags": {"$regex": tag, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]


def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": 'i'}})
    return [
        (new["title"], new["url"])
        for new in news
    ]
