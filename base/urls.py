from django.urls import path
from base.views import home, room, createRoom, updateRoom, deleteRoom, loginUser, logoutUser, signupUser, updateMessage, deleteMessage, userProfile, updateUser, topicsPage, activityPage, vote

urlpatterns = [
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('signup/', signupUser, name='signup'),

    path('', home, name="home"),
    path('room/<str:pk>/', room, name="room"),
    path('profile/<str:pk>/', userProfile, name='user-profile'),

    path('create-room/', createRoom, name="create-room"),
    path('update-room/<str:pk>/', updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', deleteRoom, name="delete-room"),
    path('update-message/<str:pk>/', updateMessage, name="update-message"),
    path('delete-message/<str:pk>/', deleteMessage, name="delete-message"),
    path('update-user/', updateUser, name='update-user'),
    path('topics/', topicsPage, name='topics'),
    path('activity/', activityPage, name='activity'),

    path('vote/<str:pk>/', vote, name='vote'),
]
