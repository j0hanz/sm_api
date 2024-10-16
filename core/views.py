from rest_framework import generics

from sm_api.permissions import IsOwnerOrReadOnly

from .models import Game, Profile
from .serializers import GameSerializer, ProfileSerializer


class ProfileList(generics.ListAPIView):
    """List all profiles."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Retrieve and update a profile."""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer) -> None:
        serializer.save()


class GameList(generics.ListCreateAPIView):
    """List all games or create a new game."""

    serializer_class = GameSerializer

    def get_queryset(self):
        return Game.objects.filter(player=self.request.user)

    def perform_create(self, serializer) -> None:
        serializer.save(player=self.request.user)


class GameDetail(generics.RetrieveAPIView):
    """Retrieve a game."""

    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
