from django.urls import path
from .views import CreatorListView, CreatorDetailView

urlpatterns = [
    path("creators/", CreatorListView.as_view(), name="creator-list"),
    path("creators/<str:pk>/", CreatorDetailView.as_view(), name="creator-detail"),
]