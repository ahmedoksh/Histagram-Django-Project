from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    text = models.CharField(max_length=2200)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text
