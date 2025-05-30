from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

# пример ответа
# {
#   "id": 1,
#   "text": "Новый прекрасный день",
#   "image": "/posts/image1.jpg",
#   "created_at": "2024-02-23T02:24:29.338414",
#   "comments": [
#     {
#       "author": 2,
#       "text": "Круто",
#       "created_at": "2024-02-23T05:12:31.054234"
#     }
#   ],
#   "likes_count": 20
# }


#  модель поста
class Post(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return f"Post by {self.author.username} at {self.created_at}"


# модель комментария
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post}"


# модель лайка
class Like(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"Like by {self.user.username} on {self.post}"


# для доп. задания
# class PostImage(models.Model):
