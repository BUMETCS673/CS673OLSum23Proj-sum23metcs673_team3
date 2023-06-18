from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# social profile
class Profile(models.Model):
    # link the profile with users
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # create new field 'followers'
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
    def __str__(self):
        return self.user.username


# Automatically create a social profile when registered
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.set([instance.profile.id])
        user_profile.save()


# posts model
class Post(models.Model):
    user = models.ForeignKey(
        User, related_name="posts", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )