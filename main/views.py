from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import random

from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from blog.models import Blog
from main.forms import ClientForm, MessageForm, MailingForm
from main.models import Client, Log, Mailing, Message
from main.task import send_mailing


class MailingHome(LoginRequiredMixin, TemplateView):
    try:
        blogs = Blog.objects.all()
        blog_counts = blogs.count()
        random_count = blog_counts if blog_counts < 3 else 3
        random_blogs = random.sample(list(blogs), random_count)
        mailing_count = Mailing.objects.all().count()
        active_mailing_count = Mailing.objects.filter(is_active=True).count()
        unique_clients_count = Client.objects.all().distinct().count()
    except:
        mailing_count = 0
        active_mailing_count = 0
        unique_clients_count = 0
        random_blogs = None

    template_name = "main/index.html"
    extra_context = {
        "title": "Главная страница",
        "mailing_count": mailing_count,
        "active_mailing_count": active_mailing_count,
        "unique_clients_count": unique_clients_count,
        "random_blogs": random_blogs,
    }


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


@login_required
def toggle_mailing_run(request, pk):

    mailing_item = get_object_or_404(Mailing, pk=pk)
    send_mailing(mailing_item)

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
    """Включение/выклчение клиента в списке рассылке на форме рассылки"""

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


class LogListView(ListView):
    model = Log
