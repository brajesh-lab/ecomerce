from django.shortcuts import render,HttpResponseRedirect
from .models import users, Post
from datetime import  date
from.models import users
from django.contrib.auth import logout

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
        email = request.POST.get("email")
        pas   = request.POST.get("password")
        print(email)
        print(pas)
        try:
            user  =  users.objects.get(email= email, password = pas)
            print(user)
            request.session['name'] = user.id
        
            context["user"] = email
            return render(request, 'success.html', context)
            return HttpResponseRedirect('success')
        except:
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
    f_name = request.session['name']
    objects = users.objects.get(id = f_name)
    
    if request.method == "POST":
          message = request.POST.get('message')
          Post.objects.create(userid = objects ,text = message, created_at= date.today,updated_at=date.today)
          
          return render(request,'message.html')
    else:
        return render(request,'message.html')