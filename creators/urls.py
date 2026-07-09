from django.urls import path
from .views import CreatorListView, CreatorDetailView
from .views import CreatorListView, CreatorDetailView, CreatorLinkView

urlpatterns = [
    path("creators/", CreatorListView.as_view(), name="creator-list"),
    path("creators/<str:pk>/", CreatorDetailView.as_view(), name="creator-detail"),
    path(
    "creators/<str:pk>/link/",
    CreatorLinkView.as_view(),
    name="creator-link"
),
]