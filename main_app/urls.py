from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('authors/', views.AuthorList.as_view(), name="author_list"),
    path('authors/new/', views.AuthorCreate.as_view(), name="author_create"),
    path('authors/<int:pk>', views.AuthorDetail.as_view(), name="author_detail"),
    path('authors/<int:pk>/update', views.AuthorUpdate.as_view(), name="author_update"),
    path('authors/<int:pk>/delete', views.AuthorDelete.as_view(), name="author_delete"),
    path('authors/<int:pk>/new', views.BookCreate.as_view(), name="book_create"),
    path('booklists/<int:pk>/books/<int:book_pk>/', views.BooklistBookAssoc.as_view(), name="booklist_book_assoc"),

]