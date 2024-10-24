# from django.contrib.auth import user_logged_in
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied

# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from main.forms import ClientForm, MessageForm, MailingForm
from main.models import Client, Mailing, Message


def index(request):
    return render(request, "main/index.html")


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        qs = Client.objects.filter(user=self.request.user)
        return qs


@login_required
def toggle_client_active(request, pk):
    client_item = get_object_or_404(Client, pk=pk)
    client_item.is_active = not client_item.is_active
    client_item.save()
    return redirect(reverse("main:list_client"))


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main:list_client")

    def form_valid(self, form):
        """Привязка пользователя к клиенту"""
        client = form.save()
        user = self.request.user
        client.user = user
        client.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    # permission_required = 'main.change_client'
    success_url = reverse_lazy("main:list_client")

    def get_object(self, queryset=None):
        """Редактировать можно только свои записи клиентов"""
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404("Доступ запрещён")
        return self.object


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("main:list_client")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message

    def get_queryset(self):
        qs = Message.objects.filter(user=self.request.user)
        return qs


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("main:list_message")

    def form_valid(self, form):
        """Привязка пользователя к сообщению"""
        message = form.save()
        user = self.request.user
        message.user = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    # permission_required = 'main.change_message'
    success_url = reverse_lazy("main:list_message")


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("main:list_message")


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    # def get_queryset(self):
    #     qs = Mailing.objects.filter(user=self.request.user)
    #     return qs


@login_required
def toggle_mailing_active(request, pk):

    current_user = request.user

    mailing_item = get_object_or_404(Mailing, pk=pk)
    mailing_user = mailing_item.user

    if current_user == mailing_user:
        pass

    mailing_item.is_active = not mailing_item.is_active
    mailing_item.save()
    return redirect(reverse("main:list_mailing"))


class MailingDetailView(DetailView):
    model = Mailing

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()
        return context


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("main:list_mailing")

    def form_valid(self, form):
        """Привязка пользователя к рассылке"""
        mailing = form.save()
        user = self.request.user
        mailing.user = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("main:list_mailing")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["clients"] = Client.objects.all()
        return context


@login_required
def toggle_mailing_client(request, mailing_pk, client_pk):
    '''Включение/выклчение клиента в списке рассылке на форме рассылки'''

    mailing_item = get_object_or_404(Mailing, pk=mailing_pk)
    client_item = get_object_or_404(Client, pk=client_pk)

    if client_item in mailing_item.clients.all():
        mailing_item.clients.remove(client_item)
    else:
        mailing_item.clients.add(client_item)

    mailing_item.save()
    return redirect(request.META.get("HTTP_REFERER", "/"))


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("main:list_mailing")
