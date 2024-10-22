from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world.")


def categories(request: HttpRequest, cat_id) -> HttpResponse:
    return HttpResponse(f"Статьи по категории {cat_id}")


def categories_by_slug(request: HttpRequest, cat_slug) -> HttpResponse:
    return HttpResponse(f'Статьи по категориями слаг {cat_slug} !!!!!!!!!')

class MyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'a': 1
        }
        return render(request, 'core/index.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Hello, POST")
