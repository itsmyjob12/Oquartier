from django.shortcuts import render
from .models import Contact


# Create your views here.
def index(request):
    datas = {}

    return render(request, "index.html", datas)

def about(request):
    datas = {}

    return render(request, "about.html", datas)

def contact(request):
    confirmation_message = None  # Initialisation du message de confirmation

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        
        # Définir le message de confirmation
        confirmation_message = "Votre message a été envoyé avec succès !"

    return render(request, 'contact.html', {'confirmation_message': confirmation_message}) # Assurez-vous d'avoir un template 'contact.html' pour afficher le formulaire


def service(request):
    datas = {}

    return render(request, "telecharger.html", datas)