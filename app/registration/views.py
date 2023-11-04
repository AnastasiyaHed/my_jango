from django.shortcuts import render, redirect
from .models import Event, Registration
from .forms import EventForm

def all_users(request):
    # все пользователи
    users = Registration.objects.all()
    return render(request, 'registration/all_users.html', {'users': users})

def user_details(request, user_id):
    #о конкретном пользователе
    user = Registration.objects.filter(id=user_id)
    return render(request, 'registration/user_details.html', {'user': user})

def registration_form(request):
    eventForm = EventForm()

    if request.method == 'POST':
        attendee_name = request.POST['attendee_name']
        attendee_email = request.POST['attendee_email']

#        registration = Registration(attendee_name=attendee_name, attendee_email=attendee_email, event=request.Вот сюда)
#        registration.save()

        return redirect('success_page')  # Перенаправление на страницу успеха

    return render(request, 'registration/registration_form.html', {"events": eventForm})



def success_page(request):
    # страница успеха
    return render(request, 'registration/success_page.html')
