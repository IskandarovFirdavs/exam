from django.contrib import admin
from car.models import CarModel, DateModel, TextModel


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)  

@admin.register(DateModel)
class DateModelAdmin(admin.ModelAdmin):
    list_display = ('price',)
    search_fields = ('price',)
    list_filter = ('price',)  

@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'quantity', 'time',)
    search_fields = ('text', 'time', 'quantity',)
    list_filter = ('quantity', 'time',) 
