from django.shortcuts import render
from django.http import HttpResponse
from book import models


def book(request):
    book_index = models.Book.objects.all().order_by('-id')
    context = {
        'book_index': book_index
    }
    return render(request, 'book.html', context)


def detail(request,book_id):
    return HttpResponse("<h2>书籍的id是："+str(book_id)+"</h2>")
