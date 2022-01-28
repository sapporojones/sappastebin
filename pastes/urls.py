# pastes/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path(
        "pastes/<uuid:pk>",
        views.PastesDetailView.as_view(),
        name="pastes-detail"
    ),
    path(
        "create",
        views.PastesCreateView.as_view(),
        name="pastes-create"
    ),
    path(
        "",
        views.PastesCreateView.as_view(),
        name="pastes-create"
    ),
]
