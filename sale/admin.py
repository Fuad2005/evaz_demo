from django.contrib import admin
from .models import Property, PropertyFeature, PropertyImage, PropertyType, PurchaseType, City
# Register your models here.
admin.site.register(PropertyFeature)
admin.site.register(PropertyType)
admin.site.register(PurchaseType)
admin.site.register(City)



class PropertyImageInline(admin.TabularInline):
    model = PropertyImage   




@admin.register(Property)
class Property(admin.ModelAdmin):
    exclude = ['updated', 'created']
    inlines = [PropertyImageInline]