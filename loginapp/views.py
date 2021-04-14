from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt
from favbooksapp import views

# Create your views here.

def index(request):
    
    context = {
        'all_users' : User.objects.all()
    }
    return render (request, 'home.html', context)
    
def create_user (request): 
    if request.method == 'POST':    
        errors = User.objects.RegistrationValidator(request.POST)
        if len(errors) >0: 
            for k,v in errors.items():
                messages.error(request, v)
                
            return redirect('/')
        
        else: 
            hashedpw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            
            new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = hashedpw)
            
            new_user_id = new_user.id
            
            request.session['user'] = new_user_id
            
            return redirect('/books')
    
    else:
        return redirect ( '/')
    
def user_login(request): 
    if request.method == 'POST':
        errors = User.objects.LoginValidator(request.POST)
        if len(errors) >0: 
            for k,v in errors.items():
                messages.error(request, v)
                
            return redirect ('/')
        
        else:
            user_log = User.objects.get(email = request.POST['email'])
            request.session['user'] = user_log.id
            return redirect('/books')
        
    else:
        return redirect('/')
    
def logout(request):
    del request.session['user']
    return redirect('/')