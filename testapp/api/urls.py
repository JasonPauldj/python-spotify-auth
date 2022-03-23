from django.urls import path
from testapp.api.views import spotify_authorize, spotify_accesstoken, spotify_user, spotify_user_playlists

urlpatterns = [
    path('', spotify_authorize ),
    path('spac',spotify_accesstoken),
    path('data',spotify_user),
    path('playlists',spotify_user_playlists)
]
