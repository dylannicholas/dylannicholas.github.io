from django.urls import path
# Import views.py from directory
from . import views

urlpatterns = [
    # When someone visits default route on app, run index function from views.py
    path("", views.index, name = "index"), 

    # When someone visits /hello/brian route, runs brian function from views.py
    path("brian", views.brian, name = "brian"),

    # Name could be any name - call greet function from views.py, then pass in Name as perimeter to function
    path("<str:name>", views.greet, name="greet")
]