from django.views.generic import View
from django.shortcuts import render
from django.core.paginator import Paginator
from posts import models as posts_models
from businesses import models as businesses_models
from . import forms


class SearchView(View):
    def get(self, request):
        keyword = request.GET.get("keyword")
        business = request.GET.get("business")
        post = request.GET.get("post")
        contents_arg = {}

        if keyword:
            form = forms.SearchForm(request.GET)
            if business and post:
                if business and post:
                    businesses = businesses_models.Business.objects.filter(
                        description__icontains=keyword
                    ).order_by("-created")[:5]

                    posts = posts_models.Post.objects.filter(
                        description__icontains=keyword
                    ).order_by("-created")[:5]

                    return render(
                        request,
                        "core/search.html",
                        {"form": form, "businesses": businesses, "posts": posts},
                    )

                else:
                    if business:
                        qs = businesses_models.Business.objects.filter(
                            description__icontains=keyword
                        ).order_by("-created")

                        paginator = Paginator(qs, 10, orphans=5)
                        page = request.GET.get("page", 1)
                        businesses = paginator.get_page(page)

                        return render(
                            request,
                            "core/search_businesses.html",
                            {"form": form, "businesses": businesses},
                        )

                    if post:
                        qs = posts_models.Post.objects.filter(
                            description__icontains=keyword
                        ).order_by("-created")

                        paginator = Paginator(qs, 10, orphans=5)
                        page = request.GET.get("page", 1)
                        posts = paginator.get_page(page)

                        return render(
                            request,
                            "core/search_posts.html",
                            {"form": form, "posts": posts},
                        )

        else:
            form = forms.SearchForm()

        contents_arg["form"] = form
        return render(request, "core/search.html", {"form": form})
