from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from .models import *

def index(request):
    books = BookList.objects.all()

    return render(request,'index.html',{'books':books})

def addbook(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.get('author')

        bookAdd = BookList(
            title = title,
            price = price,
            author = author
        )
        bookAdd.save()
        return redirect('index')
    return render(request,'addbook.html')
def readd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        author = request.POST.get('author')

        bookAdd = BookList(
            title = title,
            price = price,
            author = author
        )
        bookAdd.save()
        return redirect('addbook')
    return render(request,'addbook.html')

def edit(request,id):
    books = BookList.objects.get(pk=id)
    context = {
        'books': books,
    }

    return render(request, 'edit.html', context)

def update(request,id):
    books = BookList.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')

def deletes(request,id):
    books = BookList.objects.get(pk=id)
    books.delete()
    return redirect('/')