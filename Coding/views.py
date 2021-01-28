from django.shortcuts import render
from datetime import date
from .models import *

# Create your views here.
def problems(request):
    context = {}
    context['day'] = date.today()
    solved = 0
    easy = 0
    medium = 0
    hard = 0
    attempted = 0
    ques = []
    todo = 0
    total = 0
    for i in Programming.objects.all():
        total +=1
        ques.append(i)
        if i.status == 'Solved':
            solved+=1
            if i.difficulty == 'Easy':
                easy +=1
            elif i.difficulty == 'Moderate':
                medium +=1
            else:
                hard +=1
        elif i.status == 'Attempted':
            attempted +=1
        else:
            todo +=1
    data = {
        'ques' : ques,
        'solved' : solved,
        'Easy' : easy,
        'Medium' : medium,
        'Hard' : hard,
        'Attempted' : attempted,
        'todo' : todo,
        'total' : total
    }


    context['data'] = data
    context['category'] = Programming_Category.objects.all().order_by('category_name')
    context['companies'] = Programming_Companies.objects.all().order_by('company_name')
    return render(request,'Coding/problems.html',context)

def inside(request,var):
    context = {}
    print(var.replace("-"," ").title())
    ins = Programming.objects.get(title =  var.replace("-"," ").title())
    context['id'] = ins.id
    context['language'] = Language.objects.all()
    solved = 0
    easy = 0
    medium = 0
    hard = 0
    attempted = 0
    ques = []
    todo = 0
    total = 0
    for i in Programming.objects.all():
        total +=1
        ques.append(i)
        if i.status == 'Solved':
            solved+=1
            if i.difficulty == 'Easy':
                easy +=1
            elif i.difficulty == 'Moderate':
                medium +=1
            else:
                hard +=1
        elif i.status == 'Attempted':
            attempted +=1
        else:
            todo +=1
    data = {
        'ques' : ques,
        'solved' : solved,
        'Easy' : easy,
        'Medium' : medium,
        'Hard' : hard,
        'Attempted' : attempted,
        'todo' : todo,
        'total' : total
    }


    context['problem'] = data
    context['category'] = Programming_Category.objects.all().order_by('category_name')
    context['data'] =  ins
    return render(request,'Coding/inside.html',context)