from django.shortcuts import render,redirect
from django.contrib.auth import logout
from item.models import Category,Item
from .forms import SignupForm
import random

def index (request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    random_items = random.sample(list(items),6)
    return render(request, 'core/index.html', {
        'random_items': random_items,
        'categories': categories,
        'items': items,
    })

def about (request):
    return render(request, 'core/about.html')

def license (request):
    return render(request, 'core/license.html')

def policy (request):
    return render(request, 'core/policy.html')

def signup(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    else:
        form = SignupForm()
    
    return render(request,'core/signup.html',{
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('/') 