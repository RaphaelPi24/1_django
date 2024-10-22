from multiprocessing.resource_tracker import register

from django.urls import path, re_path, register_converter

from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.MyView.as_view()),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive, name='archive'),
    path('archive2/<year4:year>/', views.archive, name='archive2'),
]
