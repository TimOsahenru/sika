from django.contrib import admin
from .models import User, HouseType, House, HouseImage, Area
# Register your models here.


admin.site.register(User)
admin.site.register(Area)
admin.site.register(House)
admin.site.register(HouseImage)
admin.site.register(HouseType)
