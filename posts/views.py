from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

# для проверки авторства
class IsAuthorOrReadOnly(permissions.BasePermission): # класс для проверки авторства
    def has_object_permission(self, request, view, obj): # метод для проверки авторства
        if request.method in permissions.SAFE_METHODS: # если метод безопасный
            return True # возвращаем True
        return obj.author == request.user # возвращаем True если автор поста равен пользователю


# для работы с постами
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() # получаем все посты
    serializer_class = PostSerializer # сериализатор для постов
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly] # разрешения для аутентифицированных пользователей

    def perform_create(self, serializer): # создание поста
        serializer.save(author=self.request.user) # сохраняем пост


# для работы с комментариями
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all() # получаем все комментарии
    serializer_class = CommentSerializer # сериализатор для комментариев
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # разрешения для аутентифицированных пользователей

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) # сохраняем комментарий


# для работы с лайками
class LikeViewSet(viewsets.ModelViewSet): # модельный набор представлений
    queryset = Like.objects.all() # получаем все лайки
    serializer_class = LikeSerializer # сериализатор для лайков
    permission_classes = [permissions.IsAuthenticated] # разрешения для аутентифицированных пользователей

    def perform_create(self, serializer): # создание лайка
        serializer.save(user=self.request.user) # сохраняем лайк