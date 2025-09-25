from rest_framework import serializers

from django.contrib.auth.models import User

from post.models import Article, Comment, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    user = UserSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Article
        fields = (
            'id', 'title', 'content',
            'category', 'category_id', 'user', 'created_at'
        )

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        category = Category.objects.get(id=category_id)

        validated_data['user'] = self.context['request'].user
        validated_data['category'] = category
        
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    article_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = (
            'id', 'user', 'article', 'article_id',
            'content', 'created_at'
        )

    def create(self, validated_data):
        article_id = validated_data.pop('article_id')
        article = Article.objects.get(id=article_id)

        validated_data['user'] = self.context['request'].user
        validated_data['article'] = article
        
        return super().create(validated_data)