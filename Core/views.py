from django.shortcuts import render
from django.http import HttpResponse
import json
from django.contrib.auth import login, authenticate
import re
from django.contrib.auth.models import User
from .models import *
# Create your views here.

def authenticating(request):
    method = request.GET.get('method')
    if method == 'signin':
        username = request.GET.get('username')
        password = request.GET.get('password')
        if username == "":
            return HttpResponse(json.dumps(['bad','Username is incorrect!!']))
        elif password == "":
            return HttpResponse(json.dumps(['bad','Password is incorrect!!']))
        try:
            user = authenticate(username=username, password=password)
        except Exception as exp:
            return HttpResponse(json.dumps['bad',exp])
        if user is not None:
                login(request, user)
                #ins = activity(user_name3 = user,user_activity="Loged In Successfully.",activity_icon="user",color="text-info")
                #ins.save()
                print("hfu")
                return HttpResponse(json.dumps(['fine','Loged In Successfully!!']))
    
        else:
            return HttpResponse(json.dumps(['bad','Username and Password are incorrect !!']))
    else:
        if request.method == 'POST':
            
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            email = request.POST.get('email')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            
            if first == "":
                return HttpResponse(json.dumps(['bad',"First Name can't be empty!!"]))
            elif last == "":
                return HttpResponse(json.dumps(['bad',"Last Name can't be empty!!"]))
            elif not re.search(regex,email) or email == "":
                return HttpResponse(json.dumps(['bad',"Email pattern doesn't match!!"]))
            elif pass1 == "":
                return HttpResponse(json.dumps(['bad',"Password can't be empty!!"]))
            elif pass2=="":
                return HttpResponse(json.dumps(['bad',"Password Confirm can't be empty!!"]))
            elif pass1 != pass2:
                return HttpResponse(json.dumps(['bad',"Password doesn't match!!"]))
            else:
                try:
                    username = email.split('@')[0]
                    user = User.objects.create_user(username=username,
                                    email=email,
                                    password=pass1,first_name = first,last_name = last)
                    
                    login(request,user)
                    #ins = activity(user_name3 = user,user_activity="Loged In Successfully.",activity_icon="user",color="text-info")
                    #ins.save()
                    ins = Profile.objects.get(user = user)
                    ins.first_name = first
                    ins.last_name = last
                    ins.email = email
                    ins.save()
                    return HttpResponse(json.dumps(['fine','User Successfully Created!!']))
                except :
                    return HttpResponse(json.dumps(['bad','User already exists!!']))

    return HttpResponse(json.dumps(method))
def homepage(request):
    if request.user.is_authenticated:
        return render(request,'Core/frontpage.html')
    return render(request,'Core/homepage.html')
