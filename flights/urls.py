from django.urls import URLPattern, path
from .import views
from django.urls import path

urlpatterns = [
     path("",views.index,name="index"),
     path("<int:flightid>",views.flightid,name="flightid")
]