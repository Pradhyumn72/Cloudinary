from django.shortcuts import render
from .models import Student
from django.core.mail import send_mail

# Create your views here.
def landing(req):
    if req.method=="POST":
        
        n =req.POST.get('name') 
        c = req.POST.get('contact') 
        i=req.FILES.get('image') 
        a=req.FILES.get('audio') 
        v=req.FILES.get('video') 
        d= req.FILES.get("document")
        Student.objects.create(name=n,img=i,document=d,audio=a,video=v)
        send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
    )
        
    return render(req,'landing.html')
