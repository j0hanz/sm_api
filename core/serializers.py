from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Game, Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = ['id', 'username']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for the Profile model."""

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'image',
            'score',
            'highest_streak',
            'created_at',
            'updated_at',
        ]


class GameSerializer(serializers.ModelSerializer):
    """Serializer for the Game model."""

    player = UserSerializer(read_only=True)

    class Meta:
        model = Game
        fields = [
            'id',
            'player',
            'score',
            'words_attempted',
            'words_correct',
            'time_played',
            'difficulty',
            'streak',
            'date_played',
        ]
