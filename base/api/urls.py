import imp
from django.urls import path
from base.api.views import getRoutes, getRooms, getRoom


urlpatterns = [
    path('', getRoutes),
    path('rooms/', getRooms),
    path('rooms/<str:pk>/', getRoom),
]