from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from tasks.views import NewTaskForm

def index(request):
    if "name" not in request.session:
        request.session["name"] = []
    return render(request, "phonebook/index.html", {
        "name": request.session["name"]
    })

class NewContactForm(forms.Form):
    name = forms.CharField(label = "New Name")

def add(request):
    if request.method == "POST":
        form = NewContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            request.session["name"] += [name.capitalize()]
            return HttpResponseRedirect(reverse("phonebook:index"))
        else: 
            return render(request, "phonebook/add.html", {"form":form})
    return render(request, "phonebook/add.html", {
        "form": NewContactForm()
    })