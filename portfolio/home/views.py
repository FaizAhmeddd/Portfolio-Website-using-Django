from django.shortcuts import render
from home.models import Contact

def home(request):
    context = {'name': 'Faizan'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # Save the form data to the database using the Contact model
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been written into the db")

    return render(request, 'contact.html')

