from django.contrib import admin
from .models import Post, Comment, Like


admin.site.register(Post)  # регистрация модели поста
admin.site.register(Comment)  # регистрация модели комментария
admin.site.register(Like)  # регистрация модели лайка
