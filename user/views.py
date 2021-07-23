from django.shortcuts import render
from .models import users, Post
from datetime import  datetime
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        signup  = users(f_name = fname, l_name =lname, email=email, pas=password)
        signup.save()
    return render(request , 'signup.html')
def home(request):
    return render(request,'base.html')

def signin(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get("username")
        pas   = request.POST.get("email")
        user =  authenticate(request, email= email, pas = pas)
        if user:
            login(request, user)
            context["user"] = email
            return render(request, 'success.html', context)
            # return HttpResponseRedirect('success')
        else:
            context["error"] = "Provide valid credentials"
            return render(request, 'signin.html', context)
    else:
        context["error"] = "You are not logged in"
        return render(request, 'signin.html', context)
def signout(request):
    context = {}
    logout(request)
    context['error'] = "You have been logged out"
    return render(request, 'signin.html', context)


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, 'success.html', context)
def message(request):
    if request.user.is_authenticated:
        id1 = request.user
        user1 = users.objects.filter(f_name=id1)
        if user1:
            if request.method == "POST":
                message = request.POST.get('message')
                sets = Post(text = message, created_at=datetime.today, updated_at= datetime.today)
                sets.save()
        return render(request,'message.html')

        
    else:
        return render(request,'base.html')