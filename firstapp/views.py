from django.shortcuts import render,HttpResponse,redirect
from .models import Book


# Create your views here.
def home(request):
    if request.method == "POST":
        print(request.POST)#----------------------------01..
        # return HttpResponse("success") 
        name = request.POST.get("book_name")
        qty = request.POST.get("book_qty")
        price = request.POST.get("book_price")
        author = request.POST.get("book_author")
        is_pub = request.POST.get("book_is_pub")   #is_pub value=True or FALSE
        # print(name, qty, price, author, is_pub)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False
        Book.objects.create(name=name, qty=qty, price=price, author=author, is_published=is_pub)
        return redirect("home_page")
        # return HttpResponse("success") 
    elif request.method == "GET":
        #print(prequest.GET) #get query parameter
       return render(request,"home.html",{"person_name" : "BHupendra"})   #or context={ "person_name : BHupendra"}
    
def show_book(request):
    return render(request,"show_book.html")

