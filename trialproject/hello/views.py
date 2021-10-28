from django.shortcuts import render

# Remember to import HttpResponse (response from server)
from django.http import HttpResponse


# Request is HTTP request from server; To seperate out HTML from Python code, render template:
def index(request):

    # Remember to name space it, in the event there's more than one index.html file
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

# Takes HTTP request, as well as perimeter (Name), returns a HTTP Response with Name
def greet(request, name):

    # Takes additional third perimeter ('Name') - {} provides information, gives access to variable called 'Name' from urls.py path, value is name.capitalize()
    return render(request, "hello/greet.html", {
        "name" : name.capitalize()
    })
