from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, \
    HttpResponsePermanentRedirect
from django.urls import reverse
from django.views import View

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


class Myclass11:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request: HttpRequest) -> HttpResponse:
    data = {'title': 'Главная страница - шаблон',
            'menu': menu,
            'float': 28.56,
            'lst': [1, 2, 'abc', True],
            'set': {1, 2, 3, 5, 0},
            'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
            'obj': Myclass11(10, 20)
            }
    return render(request, "index.html", context=data)  # context именованный параметр


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


def categories(request: HttpRequest, cat_id) -> HttpResponse:
    return HttpResponse(f"Статьи по категории {cat_id}")


def categories_by_slug(request: HttpRequest, cat_slug) -> HttpResponse:
    print(request.GET)  # http://localhost:8000/cats/m/?params=2&a=3&b=4
    # <QueryDict: {'params': ['2'], 'a': ['3'], 'b': ['4']}>
    return HttpResponse(f'Статьи по категориями слаг {cat_slug}')


def page_not_found(request: HttpRequest, exception) -> HttpResponse:
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def archive(request: HttpRequest, year) -> HttpResponse:
    if year == 2024:
        raise Http404()
    elif year == 2025:
        return redirect('/')  # код 302
    elif year == 2026:
        return redirect('/', permanent=True)  # код 301
    elif year == 2027:
        return redirect(index)  # по названию функции во views(core)
    elif year == 2028:
        return redirect('home')  # название функции в urls(core) - Правильно!
    elif year == 2029:
        return redirect('cats', 'music')  # стандартно
    elif year == 2030:
        uri = reverse('cats', args=('music',))  # формиров адреса, не стандартно - /cats/music/
        return redirect(uri)
    elif year == 2031:
        return HttpResponseRedirect('/')  # 302
    elif year == 2032:
        return HttpResponsePermanentRedirect('/')  # 301
    # плевать какой редирект использовать
    return HttpResponse(f'<h1>Архив по годам. Выбран год: {year}</h1>')


class MyView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'a': 1
        }
        return render(request, 'core/index.html', context)

    def post(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Hello, POST")
