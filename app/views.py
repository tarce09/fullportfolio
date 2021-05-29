from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        phone=request.POST['phone']
        message=request.POST['message']
        subject=name+" with email "+email+" and phone number "+phone+" sent you a mail !"
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ['aryanraju09@gmail.com'],
            fail_silently=False,
        )
    return render(request,"index.html")