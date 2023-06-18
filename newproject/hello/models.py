from core.enums import Genders
from core.models import CoreModel
from django.db.models import IntegerField, CharField, ForeignKey, CASCADE, TextField, JSONField


class Brand(CoreModel):
    ...


class Country(CoreModel):
    ...


class Vendor(CoreModel):
    ...


class Colour(CoreModel):
    ...


class Sneakers(CoreModel):
    image = CharField(max_length=500, null=False)
    gender = IntegerField(choices=Genders.choices, null=True, default=Genders.MALE)
    note = TextField(max_length=3000, null=True, default="")
    brand = ForeignKey(Brand, on_delete=CASCADE)
    vendor = ForeignKey(Vendor, on_delete=CASCADE)
    colours = JSONField(default=list)
    country = ForeignKey(Country, on_delete=CASCADE)


