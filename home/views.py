from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .forms import SignUpForm, LoginForm, EditUserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User_Profile, User_images

# Create your views here.
def homepage(request):
    if not request.user.is_authenticated:
        return render(request, 'dating/home.html')
    else:
        return HttpResponseRedirect('/dashboard/')

def dashboard(request):
    if request.user.is_authenticated:
        user_data = User_Profile.objects.all()    
        user = request.user
        profile = User_Profile.objects.get(user=user)
        return render(request, 'dating/dashboard.html', {'user_data': user_data, 'profile': profile})
    else:
        messages.success(request, 'login first')
        return HttpResponseRedirect('/user_login/')

def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/interest/')          
    else :
        signup_form = SignUpForm()
    return render(request, 'dating/user_sign.html', {'signup_form': signup_form})

def user_interest(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            User_Profile.objects.update(interest= data['interest'])
        return render(request, 'dating/interest.html')

def user_login(request):
    if request.method == "POST":
        login_form = LoginForm(request=request, data=request.POST)
        if login_form.is_valid():
            uname = login_form.cleaned_data['username']
            upass = login_form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully.')
                return HttpResponseRedirect('/dashboard/')
            else:
                return HttpResponseRedirect('/')
    else:
        login_form= LoginForm
    return render(request, 'dating/user_login.html', {'login_form':login_form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You are logged out!')
        return HttpResponseRedirect('/user_login')
    else:
        messages.success(request, 'login required!')
        return HttpResponseRedirect('/user_login/')