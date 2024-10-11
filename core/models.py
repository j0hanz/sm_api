from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """Profile model for storing user profile data."""

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    image = CloudinaryField('image', default='nobody_pqgvzg', blank=True)
    score = models.IntegerField(default=0)
    highest_streak = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.owner.username}'s profile"


class Game(models.Model):
    """Game model for storing game data."""

    player = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='games',
    )
    score = models.IntegerField(default=0)
    words_attempted = models.IntegerField(default=0)
    words_correct = models.IntegerField(default=0)
    time_played = models.DurationField()
    difficulty = models.CharField(
        max_length=20,
        choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')],
    )
    streak = models.IntegerField(default=0)
    date_played = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_played']

    def __str__(self) -> str:
        return f"{self.player.username}'s game on {self.date_played}"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs) -> None:
    if created:
        Profile.objects.create(owner=instance)
