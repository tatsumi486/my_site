from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thankyou', views.ThankView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path('reviews/<int:pk>', views.SingleReviewView.as_view())
]