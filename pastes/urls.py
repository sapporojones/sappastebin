# pastes/urls.py

from django.urls import path

from .views import pastes_create, pastes_detail, pastes_decrypt, pastes_decrypted

urlpatterns = [
    path(
        "pastes/<uuid:pk>",
        pastes_detail,
        name="pastes-detail"
    ),
    path(
        "create",
        pastes_create,
        name="pastes-create"
    ),
    path(
        "",
        pastes_create,
        name="pastes-create"
    ),
    path(
        "decrypt/<uuid:pk>",
        pastes_decrypt,
        name="pastes-decrypt"
    ),
    path(
        "decrypted/<uuid:pk>",
        pastes_decrypted,
        name="pastes-decrypted"
    ),

]
