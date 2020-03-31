from django.shortcuts import render
from app01.models import Book
from django.http import HttpResponse
from django.shortcuts import render


def add_book(request):
    if request.method=="POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        book_obj = Book(title=title,price=price,pub_date=pub_date,publish=publish)
        book_obj.save()
        return HttpResponse("ok!")
            # redirect('/find_book')
    return render(request,'add_book.html')


def add_one(request):
    return render(request,'one.html')

