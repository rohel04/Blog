from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def inquiry(request):
    if request.method=='POST':
        full_name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        inquiry=Contact(
            fullname=full_name,
            email=email,
            subject=subject,
            message=message
        )
        inquiry.save()
        messages.info(request,'Contact submitted successfully')
        return render(request,'pages/contact.html')