from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bookindex),
    path('/add_book', views.add_book),
    path('/<int:book_id>', views.show_book),
    path('/<int:book_id>/update_title', views.update_title),
    path('/<int:book_id>/update_desc', views.update_desc),
    path('/<int:book_id>/delete', views.delete),
    path('/<int:book_id>/fav', views.add_as_fav),
    path('/<int:book_id>/non_fav', views.remove_fav),
]