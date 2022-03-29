from . models import Feedback
from django.contrib import messages
from django.shortcuts import render,redirect
from . forms import *
from django.core.mail import send_mail
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        complain = request.POST['complain']

        #for email me start#
        data={
        'name':name,
        'phone':phone,
        'email':email,
        'complain':complain,
        }
        complain = ''' 
        Message are: {}

        from: {}
        '''.format(data['complain'], data['email'])
        send_mail(data['phone'],complain, '',['rakibkhan9065@gmail.com'])
        #for email me end#

        obj = Feedback(name=name, phone=phone, email=email, complain=complain)
        obj.save()
             
    context={
    }
    return render(request, 'self/index.html',context)

