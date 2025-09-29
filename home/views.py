from django.shortcuts import render, HttpResponse
from datetime import datetime, date
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
        Quantity = request.POST.get('Quantity')
        Instructions = request.POST.get('Instructions')
        paymentMethod = request.POST.get('paymentMethod')
        name_on_card = request.POST.get('cc-name')
        card_number = request.POST.get('cc-number')
        expiration_date = request.POST.get('cc-expiration')
        cvv = request.POST.get('cc-cvv')

        contact = Contact(
            Name=Name,
            Email=Email,
            Phone=Phone,
            Address=Address,
            City=City,
            State=State,
            Quantity=Quantity,
            Instructions=Instructions,
            date=date.today(),
            paymentMethod=paymentMethod,
            name_on_card=name_on_card,
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
        )
        contact.save()
        messages.success(request, "Yay! Your order is confirmed 🎉")
    
    return render(request, 'contact.html')
