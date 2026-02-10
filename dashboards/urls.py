from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('categories',views.categories,name='categories'),
    path('categories/add/',views.add_category,name='add_category'),
    path('categories/add/edit/<int:pk>/',views.edit_category,name='edit_category'),
    path('categories/add/delete/<int:pk>/',views.delete_category,name='delete_category'),
]
