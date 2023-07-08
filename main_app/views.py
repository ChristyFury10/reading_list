from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from .models import Author, Book, BookList
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booklists"] = BookList.objects.all()
        return context
    
class About(TemplateView):
    template_name = "about.html"


class AuthorList(TemplateView):
    template_name = "author_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["authors"] = Author.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["authors"] = Author.objects.all()
            context["header"] = "Trending Authors"
        return context

class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'img', 'bio']
    template_name = "author_create.html"
    
    def get_success_url(self):
        return reverse('author_detail', kwargs={"pk": self.object.pk})

class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["booklists"] = BookList.objects.all()
        return context

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'img', 'bio']
    template_name = "author_update.html"
    
    def get_success_url(self):
        return reverse('author_detail', kwargs={"pk": self.object.pk})
    
class AuthorDelete(DeleteView):
    model = Author
    template_name = "author_delete_confirmation.html"
    success_url = "/authors/"

class BookCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        author = Author.objects.get(pk=pk)
        Book.objects.create(title=title, author=author)
        return redirect('author_detail', pk=pk)
    
class BooklistBookAssoc(View):
    
    def get(self, request, pk, book_pk):
        assoc = request.GET.get('assoc')
        if assoc == "remove":
            BookList.objects.get(pk=pk).books.remove(book_pk)
        if assoc == "add":
            BookList.objects.get(pk=pk).books.add(book_pk)
        return redirect('home')