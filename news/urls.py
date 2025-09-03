from django.urls import path

from news import views
urlpatterns = [
    path('createPost/', views.index)
]