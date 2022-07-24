from django.http import HttpResponse
from django.shortcuts import render
from .models import registration
from .form import registrationform


# Create your views here.
def home(request):
    return HttpResponse("Home page")


def contact(request, name):
    return HttpResponse("your name is : " + name)


def myhome(request):
    all_member = registration.objects.all
    return render(request, 'home.html', {'all': all_member})


def join(request):
    if request.method == "POST":
        form = registrationform(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, 'join.html', {})
    else:
        return render(request, 'join.html', {})
