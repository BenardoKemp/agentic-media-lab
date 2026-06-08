import feedparser

from feeds import RSS_FEEDS
from normalize import NewsArticle

validated_articles = []


def fetch_rss_articles():
    
    articles = []

    for feed_url in RSS_FEEDS:

        feed = feedparser.parse(feed_url)

        for entry in feed.entries:

            articles.append({
                "source": feed.feed.title, 
                "title": entry.title, 
                "link": entry.link, 
                "published": entry.get("published", ""), 
                "summary": entry.get("summary", "") 
            })
    return articles



if __name__ == "__main__": 
    
    articles = fetch_rss_articles() 

    for article in articles[:5]: 
        print(article)

    for article in articles:
        try:
            validated = NewsArticle(**article)
            validated_articles.append(validated)
        except Exception as e:
            print(f"Validation failed: {e}")    

