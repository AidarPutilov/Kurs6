from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from main.forms import ClientForm, MessageForm
from main.models import Client, Message


def index(request):
    return render(request, "main/index.html")


class ClientListView(ListView):
    model = Client


# class ClientDetailView(DetailView):
#     model = Client


class ClientCreateView(CreateView):
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


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main:clientlist")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("main:clientlist")


class MessageListView(ListView):
    model = Message


class MessageCreateView(CreateView):
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


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("main:listmessage")


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("main:listmessage")
