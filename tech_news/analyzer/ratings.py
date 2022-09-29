from operator import itemgetter
from tech_news.database import find_news


def top_5_news():
    news = find_news()
    news_sorted = sorted(
        news, key=itemgetter("comments_count", "title"), reverse=True
    )

    return [(new["title"], new["url"]) for new in news_sorted[:5]]


def top_5_categories():
    news = find_news()
    categories = [new["category"] for new in news]
    categories_sorted = sorted(
        set(categories),
        key=lambda x: (-categories.count(x), x)
    )

    return categories_sorted[:5]
