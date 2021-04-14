from django.shortcuts import render, redirect, HttpResponse
from .models import *
from loginapp.models import User 
from django.contrib import messages


# Create your views here.

def bookindex(request): 
    logged_user = User.objects.get(id = request.session['user'])
    context = {
        'user': logged_user,
        'all_books': Books.objects.all()
    }
    
    return render(request, 'book.html', context)


def add_book(request):
    logged_user = User.objects.get(id = request.session['user'])
    if request.method == 'POST':
        errors = Books.objects.BookValidator(request.POST)
        if len(errors) > 0:
            for k,v in errors.items():
                messages.error(request, v)
                
            return redirect ('/books')
        
        else:
            title = request.POST['title']
            desc = request.POST['desc']
            new_book = Books.objects.create(title = title, desc = desc, uploaded_by = logged_user)
            # logged_user.liked_users.add(new_book)
            
            new_book.liked_by.add(logged_user)
            
            new_book_id = new_book.id
            
            return redirect ('/books')
        
        
def show_book(request, book_id):
    book = Books.objects.get(id = book_id)
    logged_user = User.objects.get(id = request.session['user'])
    context = {
        'book': book, 
        'user': logged_user,
        'liked_users': book.liked_by.all()
    }
    return render (request, 'book_detail.html', context)
        
    
    
def update_title(request, book_id):
    book = Books.objects.get(id = book_id)
    logged_user = User.objects.get(id = request.session['user'])
    new_title = request.POST['updated_title']
    book.title = new_title
    book.save()
    return redirect (f'/books/{book_id}')

def update_desc(request, book_id):
    book = Books.objects.get(id = book_id)
    logged_user = User.objects.get(id = request.session['user'])
    new_desc = request.POST['updated_desc']
    book.desc = new_desc
    book.save()
    return redirect (f'/books/{book_id}')

def delete(request, book_id):
    book = Books.objects.get(id = book_id)
    book.delete()
    return redirect ('/books')

def add_as_fav(request, book_id):
    book = Books.objects.get(id = book_id)
    logged_user = User.objects.get(id = request.session['user'])
    book.liked_by.add(logged_user)
    return redirect (f'/books/{book_id}')

def remove_fav(request, book_id):
    book = Books.objects.get(id = book_id)
    logged_user = User.objects.get(id = request.session['user'])
    book.liked_by.remove(logged_user)
    return redirect (f'/books/{book_id}')
