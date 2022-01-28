from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Pastes

class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class PastesDetailView(DetailView):
    model = Pastes

class PastesCreateView(CreateView):
    model = Pastes
    fields = ["paste_body",]

    success_url = "pastes/{id}"
