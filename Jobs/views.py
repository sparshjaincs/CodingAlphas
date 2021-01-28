from django.shortcuts import render
from .jobs import Jobs, Hiring
import json
from Core.models import *
from django.http import HttpResponse
# Create your views here.
def jobs(request):
    context = {}
    '''
    hp = Hiring()
    context['data'] = hp.extract()
    '''
   
    return render(request,'Jobs/homepage.html',context)
def current_hiring(self):
    hp = Hiring()
    data = hp.extract()
    return HttpResponse(json.dumps(data))


def show_jobs(request):
    context = {}
    company = request.GET.get('company').capitalize()
    city = request.GET.get('city').capitalize()
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)

    if page >= 1 and page <=4:
        pagination = {
            'previous':['disabled',page],
            'active':page,
            'pages':[1,2,3,4,5],
            'next':6,
            
        }
    else:
            pagination = {
                'previous':['active',page-1],
                'active':page,
                'pages':[page-2,page-1,page,page+1,page+2],
                'next':[page+3],
            }
    context['pagination'] = pagination
    if not Job_Search.objects.filter(user = request.user,title=company,location=city).exists():
        instance = Job_Search(user=request.user,title=company,location=city)
        instance.save()

    context['company'] = company
    context['city'] = city

    
    
    j1 = Jobs(company,city,page)
    data = j1.select()
    context['data'] = data

   
    context['recent'] = Job_Search.objects.filter(user = request.user)

    return render(request,'Jobs/show_jobs.html',context)
def companies(request):
    context = {}
    if request.method == 'POST':
        job = request.POST.get('job')
        instance = Company()
        data = instance.find_information(job)
        context['data'] = data
    return render(request,'coding/companies.html',context)

def company_info(request,name):
    context = {}
    job = name

    if request.method == 'POST':
        job = request.POST.get('job')
    '''
    instance = Company()
    data = instance.find_information(job)
    context['data'] = data
    '''
    return render(request,'coding/companies.html',context)
