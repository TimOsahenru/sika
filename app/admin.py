from django.contrib import admin
from .models import Agent, House, Location, HouseType


admin.site.register(Agent)
admin.site.register(House)
admin.site.register(Location)
admin.site.register(HouseType)

