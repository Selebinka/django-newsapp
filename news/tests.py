from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Article, FavoriteArticle


INPUT_DATA = dict(
    source="source",
    author="author",
    title="title",
    description="description",
    url="https://www.example.com/",
    url_to_image="https://www.example.com/",
    published_at="2020-11-22T14:13:00Z",
    content="content"
)


class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test', password='12test12', email='test@example.com')
        self.article = Article.objects.create(publisher=self.user, **INPUT_DATA)
        self.article_without_publisher = Article.objects.create(**INPUT_DATA)

    def tearDown(self):
        self.article.delete()
        self.article_without_publisher.delete()
        self.user.delete()

    def test_publisher_field(self):
        self.assertEquals(self.article.publisher, self.user)
        self.assertEquals(self.article_without_publisher.publisher, None)

    def test_source_field(self):
        self.assertEquals(self.article.source, 'source')

    def test_author_field(self):
        self.assertEquals(self.article.author, 'author')

    def test_title_field(self):
        self.assertEquals(self.article.title, 'title')

    def test_description_field(self):
        self.assertEquals(self.article.description, 'description')

    def test_url_field(self):
        self.assertEquals(self.article.url, 'https://www.example.com/')

    def test_url_to_image_field(self):
        self.assertEquals(self.article.url_to_image, 'https://www.example.com/')

    def test_published_at_field(self):
        self.assertEquals(self.article.published_at, '2020-11-22T14:13:00Z')

    def test_content_field(self):
        self.assertEquals(self.article.content, 'content')


class FavoriteArticleModelTest(TestCase):

    def setUp(self):
        # Set up non-modified objects used by all test methods
        self.article = Article.objects.create(**INPUT_DATA)
        self.user = get_user_model().objects.create(username='test', password='12test12', email='test@example.com')
        self.favorite_article = FavoriteArticle.objects.create(article=self.article, user=self.user)

    def tearDown(self):
        self.article.delete()
        self.user.delete()

    def test_article_field(self):
        self.assertEquals(self.favorite_article.article, self.article)

    def test_user_field(self):
        self.assertEquals(self.favorite_article.user, self.user)