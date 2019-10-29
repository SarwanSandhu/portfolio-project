from .models import Job

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms

def home(request):
    jobs=Job.objects
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']
        if name and email and message:
            try:
                send_mail(name, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request,'jobs/home.html',  {'jobs':jobs})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def resume(request):
    resume = Job.objects
    return render(request, 'jobs/resume.html',{'resume1':resume})


# from .models import Job
#
# from django.core.mail import send_mail, BadHeaderError
# from django.http import HttpResponse, HttpResponseRedirect
# from django.shortcuts import render, redirect
# from .forms import ContactForm
#
#
# def home(request):
#     jobs=Job.objects
#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(name, message, email, ['admin@example.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request,'jobs/home.html',  {'jobs':jobs,'form':form})
#
#
# def successView(request):
#     return HttpResponse('Success! Thank you for your message.')
#
# def resume(request):
#     resume = Job.objects
#     return render(request, 'jobs/resume.html',{'resume1':resume})
