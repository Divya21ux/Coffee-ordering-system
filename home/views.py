from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def menu(request):
    return render(request, 'menu.html')

def contact(request):
    if request.method == "POST":
        print(request.POST) 

        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone') 
        Address = request.POST.get('Address')
        City = request.POST.get('City')
        State = request.POST.get('State')
        CoffeeType = request.POST.get('CoffeeType')
        Quantity = request.POST.get('Quantity')
        Instructions = request.POST.get('Instructions')

        from datetime import date
        contact = Contact(
            Name=Name,
            Email=Email,
            Phone=Phone,
            Address=Address,
            City=City,
            State=State,
            CoffeeType=CoffeeType,
            Quantity=Quantity,
            Instructions=Instructions,
            date=date.today()
        )
        contact.save()
        messages.success(request, "Yay! Your order is confirmed 🎉")
    return render(request, 'contact.html')
