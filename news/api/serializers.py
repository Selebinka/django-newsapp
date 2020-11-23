from rest_framework import serializers
from ..models import Article, FavoriteArticle


class ArticleSerializer(serializers.ModelSerializer):
    publisher = serializers.SerializerMethodField('get_publisher')

    class Meta:
        model = Article
        fields = '__all__'

    def get_publisher(self, obj):
        if not obj.publisher:
            return 'Admin'
        return obj.publisher


class FavoriteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteArticle
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'article': {'read_only': True}
        }

    def create(self, validated_data):
        user = self.context['request'].user
        article_id = self.context['view'].kwargs.get('article_id')
        return FavoriteArticle.objects.create(user=user, article=article_id)
