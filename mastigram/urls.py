from django.urls import path
from mastigram.views import *

urlpatterns = [
    path('',home_page,name='home_page'),
    path('uppost/',uploadpost,name='uploadpost'),
    path('reel-feed',reel_page,name='reel_page'),
    path('post-feed/',post_page,name='post_page'),
    path('post/', post_list, name='post_list'),
    path('upreel/',uploadreel,name='uploadreel'),
    path('upstory/',uploadstory,name='uploadstory'),
    path('upvideo/',uploadvideo,name='uploadvideo'),
    path('profile/',profile_page,name='profile_page'),
    path('video/',video_page,name='video_page'),
]
