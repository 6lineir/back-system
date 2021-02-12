from django.shortcuts import render,redirect
from .models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .form import EditProfileForm
# Create your views here.
def index(request):

  return render(request, "registration/index.html")

@login_required
def profile(request):
    if request.method == "POST":
      form = EditProfileForm(request.POST, instance=request.user)
      if form.is_valid:
        form.save()
        return redirect('accounts:profile')
    else:
      form = EditProfileForm(instance=request.user)
      args = {'form': form}
    return render(request, "registration/profile.html", args )

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('accounts:profile')
        else:
            return render (request,'registration/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'registration/login.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'registration/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('accounts:profile')
        else:
            return render (request,'registration/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'registration/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('accounts:indexcc')