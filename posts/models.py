from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image


class Posts(models.Model):
    caption = models.CharField(max_length=2200)
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="PostsImages")
    user = ForeignKey(User, on_delete=models.CASCADE, related_name="userposts")

    def __str__(self):
        return f"Post {self.id} ({self.user.username})'s"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        img.save(self.image.path)
