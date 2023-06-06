from django.shortcuts import render, redirect
from .models import Pass
from datetime import datetime
from .forms import newPass
# Create your views here.


def index(request):
    passw = Pass.objects.all().filter(deleted=False)
    return render(request, "password/index.html", {'pass': passw})


def remove(request, id):
    p = Pass.objects.get(id=id)
    if p.deleted == False:
        p.deleted = True
    p.save()
    return redirect(request.META.get('HTTP_REFERER'))


def Add(request):
    p = Pass.objects.all().filter(deleted=False)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = newPass(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data["email"]
            password= form.cleaned_data["password"]
            ps = Pass(email=email, password= password)
            ps.save()
            return render(request,"password/index.html/",{'form': form, 'pass':p})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = newPass()

    return render(request, "password/addPass.html", {'form': form, 'pass': p})
