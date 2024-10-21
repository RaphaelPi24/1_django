from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('test/', views.MyView.as_view()),
    path('cats/<int:cat_id>/', views.categories, name='cats'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
]
