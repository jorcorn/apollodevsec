from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


# Create your views here.

def homepage(request):
    if request.method == 'GET':
        form = ContactForm

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            try:
                send_mail(subject, message, email, ['apollodevsec@gmail.com'])
                print("it worked")
            except:
                return HttpResponse('Invalid header found')
                print("Didn't work")

    return render(request, 'page/home.html', {'form': form})
