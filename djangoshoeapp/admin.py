from django.contrib import admin
from .models import Shoes


# Register your models here.
class ShoesAdmin(admin.ModelAdmin):
    list_display = ('shoename', 'shoeimage', 'shoeprice')


admin.site.register(Shoes, ShoesAdmin)
