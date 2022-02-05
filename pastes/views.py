from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.views.generic.edit import FormView
import os
from django.contrib import messages
from .models import Pastes
from .forms import PastesForm
from dataclasses import dataclass


@dataclass
class FormAttrs:
    pk: str


transient_data = FormAttrs(pk="")


class IAmLazyMixin:
    def form_valid(self, form):
            # This method is called when valid form data has been POSTed.
            # It should return an HttpResponse.
            cleaned = form.cleaned_data

            form_data = Pastes(
                paste_body = cleaned['paste_body'],

                encrypted_flag = cleaned['password_protect']
            )
            data_obj = form_data.save()
            self.pk = data_obj.pk
            # PK_TEMP = data_obj.pk

            return super().form_valid(form)


class LockedView(LoginRequiredMixin):
    login_url = "admin:login"


class PastesDetailView(DetailView):
    model = Pastes


class PastesCreateView(FormView):
    template_name = "pastes/pastes_form.html"
    model = Pastes
    form_class = PastesForm
    # fields = ["paste_body",]

    success_url = '/pastes/{pk}'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # saved = form.save()
        # self.pk = saved.pk
        cleaned = form.cleaned_data

        form_data = Pastes(
            paste_body=cleaned['paste_body'],

            # encrypted_flag=cleaned['password_protect']
        )
        # password protect logic goes here

        form_data.save()
        transient_data.pk = form_data.pk
        # print(form_data.pk)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pastes-detail', kwargs={'pk': transient_data.pk})
