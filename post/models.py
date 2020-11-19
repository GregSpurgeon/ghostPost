from django.db import models
from django.utils import timezone

# Create your models here.


class PostType(models.Model):
    post_type = models.CharField(max_length=5)

    def __str__(self):
        return self.post_type


class Post(models.Model):
    is_boast = models.ForeignKey(PostType, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    vote_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
