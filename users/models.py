from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default="DefaultPP.jpg", upload_to="ProfilePictures")
    status = models.CharField(max_length=300, default="")
    name = models.CharField(max_length=150, default="")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # this is to resize the image
            img.save(self.picture.path)  # rewrite the image


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=CASCADE, related_name="followers")
    following = models.ForeignKey(User, on_delete=CASCADE, related_name="followings")
