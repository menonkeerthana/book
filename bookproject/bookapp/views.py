from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Book
from . forms import BookForm

# Create your views here.
def index(request):
    book=Book.objects.all()
    return render(request,'index.html',{'book_list':book})

def detail(request,id):
    book=Book.objects.get(id=id)
    return render(request,'detail.html',{'book':book})
# return HttpResponse("this is book no %s" %id)

def add_book(request):
    if request.method=='POST':
        name = request.POST.get('name')
        auth = request.POST.get('auth')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        price = request.POST.get('price')
        img = request.FILES['img']

        book=Book(name=name,auth=auth,desc=desc,year=year,price=price,img=img)
        book.save()
    return render(request,'add.html')

def update(request,id):
    book=Book.objects.get(id=id)
    form=BookForm(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':book})


def delete(request,id):
    if request.method=='POST':
        book=Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')
