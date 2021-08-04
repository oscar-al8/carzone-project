from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Team
from cars.models import Car

# Create your views here.

def home(request):

    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    
    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
        'year_search': year_search,
    }
    return render(request, 'pages/home.html', data) 

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website!'
        message_body = 'Name: ' + name + '.\nEmail: ' + email + '.\nPhone: ' + phone + '.\nSubject: ' + subject + '.\nMessage: ' + message

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'blaxterbos@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us! We will come back to you shortly!')
        return redirect('contact')

    return render(request, 'pages/contact.html')