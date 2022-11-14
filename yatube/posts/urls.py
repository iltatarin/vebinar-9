from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.index, name="index"),
    # "Надо исправить": Должен использоваться PathConverter slug,
    # name тоже обязателен
    path("group/<slug:slug>/", views.group_posts, name="group_list")
]
