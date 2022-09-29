import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def search_menu(response):
    if response == "1":
        title = input("Digite o título:")
        return search_by_title(title)
    if response == "2":
        date = input("Digite a data no formato aaaa-mm-dd:")
        return search_by_date(date)
    if response == "3":
        tag = input("Digite a tag:")
        return search_by_tag(tag)

    category = input("Digite a categoria:")
    return search_by_category(category)


def top_filter_menu(response):
    if response == "5":
        return top_5_news()

    if response == "6":
        return top_5_categories()

    sys.stdout.write("Encerrando script\n")


def leave_menu(response):
    if response == "7":
        return sys.stdout.write("Encerrando script\n")

    return sys.stderr.write("Opção inválida\n")


def analyzer_menu():
    response = input(
        """
Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.
    """
    )

    if response == "0":
        amount = input("Digite quantas notícias serão buscadas:")
        get_tech_news(int(amount))
    elif response.isdigit() and 1 <= int(response) <= 6:
        news = (
            search_menu(response)
            if int(response) < 5
            else top_filter_menu(response)
        )
        for new in news:
            sys.stdout.write(new)
    else:
        leave_menu(response)
