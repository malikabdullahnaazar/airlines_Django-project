from django.contrib import admin
from flights.models import Airport,flight,passanger
# from models import flight 
# Register your models here.
admin.site.register(Airport)
admin.site.register(flight)
admin.site.register(passanger)