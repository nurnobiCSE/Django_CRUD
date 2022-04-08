from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.deletes, name='delete'),
    path('update/<id>/', views.update, name='update'),
    path('books/add', views.addbook, name='addbook'),
    path('books/readd/', views.readd, name='readd'),
]
