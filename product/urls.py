from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.HomeView.as_view(), name="main"),
    path("search/", views.SearchView.as_view(), name="search")
]