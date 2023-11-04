from django.shortcuts import render, redirect
from .models import Event, Registration

def all_users(request):
    # все пользователи
    users = Registration.objects.all()
    return render(request, 'registration/all_users.html', {'users': users})

def user_details(request, user_id):
    #о конкретном пользователе
    user = Registration.objects.get(pk=user_id)
    return render(request, 'registration/user_details.html', {'user': user})

def registration_form(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        attendee_name = request.POST['attendee_name']
        attendee_email = request.POST['attendee_email']

        registration = Registration(event=event, attendee_name=attendee_name, attendee_email=attendee_email)
        registration.save()

        return redirect('success_page')  # Перенаправление на страницу успеха

    return render(request, 'registration/registration_form.html', {'event': event})

def success_page(request):
    # страница успеха
    return render(request, 'registration/success_page.html')
