from django.conf import settings
from newsapi import NewsApiClient

from newsapp.celery import app
from .models import Article

news_api = NewsApiClient(api_key=settings.NEWS_API_KEY)


@app.task
def get_news():
    response = news_api.get_everything(sources='bbc-news,the-verge')
    if articles := response.get('articles'):
        for article in articles:
            Article.objects.create(
                source=article['source']['name'],
                author=article['author'],
                title=article['title'],
                description=article['description'],
                url=article['url'],
                url_to_image=article['urlToImage'],
                published_at=article['publishedAt'],
                content=article['content'],
            )
