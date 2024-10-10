from django.urls import path

from .views import GameDetail, GameList, ProfileDetail, ProfileList

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('games/', GameList.as_view(), name='game-list'),
    path('games/<int:pk>/', GameDetail.as_view(), name='game-detail'),
]
