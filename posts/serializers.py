from rest_framework import serializers
from .models import Post, Comment, Like


# сериализатор для комментариев
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:  # мета класс для комментариев
        model = Comment
        fields = ['id', 'author', 'text', 'created_at']


# сериализатор для постов
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:  # мета класс для постов
        model = Post
        fields = [
            'id', 'text', 'image', 'created_at',
            'likes_count', 'comments', 'author'
        ]
        read_only_fields = ['author', 'created_at']

    def get_likes_count(self, obj):  # метод для получения количества лайков
        return obj.likes.count()


# сериализатор для лайков
class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:  # мета класс для лайков
        model = Like
        fields = ['id', 'post', 'user']
        read_only_fields = ['user']
