from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pastes
from .forms import PastesForm, PasswordEntry
from dataclasses import dataclass

# for password support
import base64
import os
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


@dataclass
class FormAttrs:
    pk: str


base = "pcJoe1UDu1bNICpo9DTKfPY3tpb9Fj29Ie"
salt = base.encode()


def pastes_create(request):
    context = {}
    form = PastesForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():

            cleaned = form.cleaned_data
            # password protect logic goes here
            if cleaned['password_protect']:
                entered_password = cleaned['encryption_key']
                password = entered_password.encode()
                # salt = os.urandom(16)

                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=128000,
                )
                key = base64.urlsafe_b64encode(kdf.derive(password))
                f = Fernet(key)
                raw_body = cleaned['paste_body']
                encoded_body = raw_body.encode()
                token = f.encrypt(encoded_body)
                token = token.decode()
                form_data = Pastes(
                    paste_body=token,  # paste_body=cleaned['paste_body'],

                    encrypted_flag=cleaned['password_protect'],
                )
                form_data.save()

                # print(form_data.pk)
                context['pk'] = form_data.pk
                return redirect('pastes-detail', form_data.id)

            form_data = Pastes(
                paste_body=cleaned['paste_body'],

                encrypted_flag=cleaned['password_protect']
            )
            form_data.save()

            # print(form_data.pk)
            context['pk'] = form_data.id
            return redirect('pastes-detail', form_data.id)
    context['form'] = form
    return render(request, 'pastes/pastes_form.html', context)


def pastes_detail(request, pk):
    context = {"pastes": Pastes.objects.get(id=pk)}
    eval_obj = Pastes.objects.get(id=pk)

    if eval_obj.encrypted_flag:
        request.session['payload'] = eval_obj.paste_body
        return redirect('pastes-decrypt', pk)

    return render(request, "pastes/pastes_detail.html", context)


def pastes_decrypt(request, pk):
    form = PasswordEntry(request.POST or None)
    context = {}
    if request.method == 'POST':
        if form.is_valid():
            cleaned = form.cleaned_data

            raw_key = cleaned['user_password']
            bytes_key = raw_key.encode()
            b64_key = base64.b64encode(bytes_key)
            request.session["inconspicuous_text"] = b64_key.decode()
            return redirect('pastes-decrypted', pk)
    context['form'] = form
    return render(request, 'pastes/password.html', context)


def pastes_decrypted(request, pk):
    # context = {"pastes": Pastes.objects.get(id=pk)}
    context = {}
    query = Pastes.objects.get(id=pk)
    context['query'] = query
    try:
        b64_key = request.session["inconspicuous_text"]
    except KeyError:
        return redirect('pastes-decrypt', pk)
    bytes_key = base64.b64decode(b64_key)
    # decoded_key = bytes_key.decode()
    # salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=128000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes_key))
    f = Fernet(key)
    payload_raw = query.paste_body
    payload = payload_raw.encode()
    try:
        clean_out = f.decrypt(payload)
        template_out = clean_out.decode()
    except:
        # move to decrypt
        request.session['payload'] = query.paste_body
        return redirect('pastes-decrypt', pk)
    context['template_out'] = template_out
    return render(request, "pastes/pastes_decrypted.html", context)
