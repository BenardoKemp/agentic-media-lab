
def deduplicate_articles(articles):
    seen = set()

    unique_articles = []

    for article in articles:
        title = article.title.lower()
        if title not in seen:
            seen.add(title)
            unique_articles.append(article)

    return unique_articles