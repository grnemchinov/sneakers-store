from django.contrib import admin
from hello.models import Brand, Country, Vendor, Colour, Sneakers


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    ...


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    ...


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    ...


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    ...


@admin.register(Sneakers)
class SneakersAdmin(admin.ModelAdmin):
    ...



