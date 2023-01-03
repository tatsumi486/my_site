from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path("posts", views.posts, name = "post"),
    path("posts/<slug:slug>", views.post_details, name = "post-detail-page") #checks that slug is slug (char and underscore and numbers)
]
