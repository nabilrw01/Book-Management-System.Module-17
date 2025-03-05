from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home/Landing page
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('books/', views.book_list, name='book_list'),  # Main book list
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
]
