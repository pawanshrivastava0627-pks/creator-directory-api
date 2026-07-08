from django.urls import path
from .views import CreatorListView

urlpatterns = [
    path("creators/", CreatorListView.as_view(), name="creator-list"),
]