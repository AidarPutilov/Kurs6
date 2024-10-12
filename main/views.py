from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from main.forms import ClientForm, MessageForm
from main.models import Client, Message


def index(request):
    return render(request, "main/index.html")


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


# class ClientDetailView(DetailView):
#     model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main:clientlist")

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
    success_url = reverse_lazy("main:clientlist")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("main:clientlist")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("main:listmessage")

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
    success_url = reverse_lazy("main:listmessage")


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("main:listmessage")


class MailingListView(LoginRequiredMixin, ListView):
    model = Message


# class MailingCreateView(LoginRequiredMixin, CreateView):
#     model = Mailing
#     form_class = MailingForm
#     success_url = reverse_lazy("main:listmailing")

#     def form_valid(self, form):
#         """Привязка пользователя к сообщению"""
#         mailing = form.save()
#         user = self.request.user
#         mailing.user = user
#         mailing.save()
#         return super().form_valid(form)


# class MailingUpdateView(LoginRequiredMixin, UpdateView):
#     model = Mailing
#     form_class = MailingForm
#     success_url = reverse_lazy("main:listmailing")


# class MailingDeleteView(LoginRequiredMixin, DeleteView):
#     model = Mailing
#     success_url = reverse_lazy("main:listmailing")
