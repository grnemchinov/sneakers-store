from core.enums import Genders
from core.models import CoreModel
from django.db.models import IntegerField, CharField, ForeignKey, CASCADE, \
    TextField, JSONField


class Brand(CoreModel):
    ...


class Country(CoreModel):
    ...


class Vendor(CoreModel):
    ...


class Colour(CoreModel):
    ...


class Feedback(CoreModel):
    content = TextField(max_length=3000, null=True, default="")


class Sneakers(CoreModel):
    image = CharField(max_length=500, null=False)
    gender = IntegerField(choices=Genders.choices, null=True,
                          default=Genders.MALE)
    note = TextField(max_length=3000, null=True, default="")
    brand = ForeignKey(Brand, on_delete=CASCADE)
    vendor = ForeignKey(Vendor, on_delete=CASCADE)
    colours = JSONField(default=list)
    country = ForeignKey(Country, on_delete=CASCADE)


class WishList(object):

    def __init__(self, request):
        self.session = request.session
        items = self.session.get("wishlist", None)

        if not items:
            self.items = set()
            self.session["wishlist"] = []
        else:
            self.items = set(items)

    def __iter__(self):
        items = Sneakers.objects.filter(id__in=list(self.items))
        for item in items:
            yield item

    def add(self, item):
        self.items.add(item)
        self.save()

    def save(self):
        self.session["wishlist"] = list(self.items)
        self.session.modified = True

    def remove(self, item):
        self.items.remove(item)
        self.save()

    def clear(self):
        self.items = set()
        self.session["wishlist"] = []
        self.save()



