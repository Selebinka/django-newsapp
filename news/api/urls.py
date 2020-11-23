from django.urls import re_path
from . import views

urlpatterns = [
    re_path("feed/$", views.ArticleList.as_view(), name="article_list"),
    re_path(r"feed/(?P<pk>\d+)/", views.ArticleDetail.as_view(), name="article_detail"),
    re_path("favorites/$", views.FavoriteArticleList.as_view(), name="favorite_article_list"),
    re_path(r"favorites/save/(?P<article_id>\d+)/", views.FavoriteArticleCreate.as_view(), name="add_to_favorite"),
    re_path(r"favorites/(?P<pk>\d+)/", views.FavoriteArticleDetail.as_view(), name="favorite_article_detail"),
]
