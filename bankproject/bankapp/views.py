from . models import District,Branches
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import redirect

# Create your views here.
def home(request):
   return render(request,"base.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request,"Username Taken")
                 return redirect('register')
             else:
                 Users = User.objects.create_user(username=username,password=password)
                 Users.save();
                 return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
    return render(request,"register.html")


def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request,user)
         return render(request,"newpage.html")
      else:
         messages.info(request, "invalid credentials")
         return redirect('login')
   return render(request, "login.html")



def newpage(request):
   return render(request,"form.html")

def form(request):
     if request.method=='POST':
        username1 = request.POST['username1']
        if username1 is not None:
            messages.info(request, "Application Accepted")
     dist = District.objects.All()
     dist_id = request.GET.get('dist_id')
     branches = Branches.objects.filter(dist_id=dist_id).all()
     return render(request, 'form.html', {'branches': branches})





