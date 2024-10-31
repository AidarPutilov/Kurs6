from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from blog.models import Blog
from django.urls import reverse, reverse_lazy


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "text", "picture")
    success_url = reverse_lazy("blog:list_blog")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "text", "picture")
    success_url = reverse_lazy("blog:list_blog")

    def get_success_url(self):
        return reverse("blog:detail_blog", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list_blog")
