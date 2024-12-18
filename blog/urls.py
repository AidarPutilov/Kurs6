from django.urls import path
from django.views.decorators.cache import cache_page
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path("list_blog", BlogListView.as_view(), name="list_blog"),
    path(
        "detail_blog/<int:pk>/",
        cache_page(60)(BlogDetailView.as_view()),
        name="detail_blog",
    ),
    path("create_blog/", BlogCreateView.as_view(), name="create_blog"),
    path("update_blog/<int:pk>/", BlogUpdateView.as_view(), name="update_blog"),
    path("delete_blog/<int:pk>/", BlogDeleteView.as_view(), name="delete_blog"),
]
