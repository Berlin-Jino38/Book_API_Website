from django.shortcuts import render,redirect
from .models import Author,Book
from django.http import HttpResponse
from .forms import SignupForm
# Create your views here.
def Auther_view(request):
    authors = Author.objects.all()
    return render(request,'myApp/index.html',{'authors':authors})

def Book_view(request, name):
    books = Book.objects.filter(author__first_name=name)
    return render(request, 'myApp/book.html', {'books': books})

def search_view(request):
    query = request.GET.get('q')
    if query:
        items = Author.objects.filter(first_name__icontains=query).order_by('-first_name')
       
    else:
        # Handle the case when 'q' is not provided, for example, display all categories.
        items = Author.objects.all().order_by('-first_name')  
    return render(request, 'myApp/index.html', {'authors': items})

def signup(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login/')

    else:
        form=SignupForm()
    return render(request, 'myApp/signup.html', {'form': form})

