from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('test/', views.MyView.as_view()),
    path('test2/', views.MyTemplateView.as_view()),
    path('test_list/', views.MyListView.as_view()),
    path('test_list/<int:pk>/', views.MyDetailView.as_view()),
    path('cats/<int:cat_id>/', views.categories, name='cats'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug),
]
