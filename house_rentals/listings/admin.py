from django.contrib import admin

# Register your models here.
from .models import Property, CustomUser, Review, PropertyImage, Favorite

admin.site.register(Property)
admin.site.register(CustomUser)
admin.site.register(Review)
admin.site.register(PropertyImage)
admin.site.register(Favorite)