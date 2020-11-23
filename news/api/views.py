from rest_framework import generics

from .serializers import ArticleSerializer, FavoriteArticleSerializer
from ..models import Article, FavoriteArticle


class ArticleList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of news and create.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(generics.RetrieveDestroyAPIView):
    """
    API endpoint that represents a single news.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FavoriteArticleList(generics.ListAPIView):
    """
    API endpoint representing the user's favorites news.
    """
    queryset = FavoriteArticle.objects.all()
    serializer_class = FavoriteArticleSerializer


class FavoriteArticleCreate(generics.CreateAPIView):
    """
    API endpoint add news to favorites.
    """
    queryset = FavoriteArticle.objects.all()
    serializer_class = FavoriteArticleSerializer


class FavoriteArticleDetail(generics.RetrieveDestroyAPIView):
    """
    API endpoint that represents a single favorite news.
    """
    queryset = FavoriteArticle.objects.all()
    serializer_class = FavoriteArticleSerializer
