from django.http import HttpResponse
from django.shortcuts import render
from templates import *

import datetime

def home(request):
    print("Welcome")
    isActive=True
    # if request.method=='POST':
    #     check=request.POST.get("check")
    #     print(check)
        
    if request.method=='POST':
        click=request.POST.get("click")
        print(click)
        if click is None: isActive=False
        else: isActive=True
        
    date=datetime.datetime.now()
    name="Swarup Dash"
    list_of_programs=[
        'wap to check even or odd',
        'wap to check prime number',
        'wap to print all prime number from 1 to 100',
        'wap to print pascals triangle'
    ]
    student={
        'student_name': "Swarup",
        'student_college': "XYZ",
        'student_city': "Bhubaneswar"
    }
    data={
        'date': date,
        'isActive':isActive,
        'name':name,
        'list_of_programs':list_of_programs,
        'student':student
    }
    return render(request, "home.html", data)

def about(request):
    return render(request, "about.html", { })

def contact(request):
    return render(request, "contact.html", { })

def mytemp(request):
    return render(request, "mytemp.html", {})
