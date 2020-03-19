from django.shortcuts import render
from django.views.generic import ListView, View
from django.urls import reverse
from django.core.paginator import Paginator
from . import models


class HomeView(ListView):
    """ Home View Definition """

    model = models.Product
    paginate_by = 20
    paginate_orphans = 5
    ordering = "category"
    context_object_name = "products"


class SearchView(View):
    def get(self, request):
        title = request.GET.get("title")
        
        if title:
            # for maintenance
            filter_args = {}
            filter_args["title__startswith"] = title
            qs = models.Product.objects.filter(**filter_args).order_by("category")

            paginator = Paginator(qs, 20, orphans=5)
            page = request.GET.get("page", 1)
            products = paginator.get_page(page)

            return render(request, "product/search.html", {"products": products, "page_obj": products})
        else:
            reverse("products:main")