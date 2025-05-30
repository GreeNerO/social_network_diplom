from rest_framework import viewsets, permissions
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer


# для проверки авторства
class IsAuthorOrReadOnly(permissions.BasePermission):
    # метод проверки авторства
    def has_object_permission(self, request, view, obj):
        # если метод безопасный
        if request.method in permissions.SAFE_METHODS:
            return True  # возвращаем True
        # True если автор поста = пользователю
        return obj.author == request.user


# для работы с постами
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # получаем все посты
    serializer_class = PostSerializer  # сериализатор для постов
    # разрешения для аутентифицированных пользователей
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]

    def perform_create(self, serializer):  # создание поста
        serializer.save(author=self.request.user)  # сохраняем пост


# для работы с комментариями
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()  # получаем все комментарии
    serializer_class = CommentSerializer  # сериализатор для комментариев
    # разрешения для аутентифицированных пользователей
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):  # создание комментария
        serializer.save(user=self.request.user)  # сохраняем комментарий


# для работы с лайками
class LikeViewSet(viewsets.ModelViewSet):  # модельный набор представлений
    queryset = Like.objects.all()  # получаем все лайки
    serializer_class = LikeSerializer  # сериализатор для лайков
    # разрешения для аутентифицированных пользователей
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def perform_create(self, serializer):  # создание лайка
        serializer.save(user=self.request.user)  # сохраняем лайк
