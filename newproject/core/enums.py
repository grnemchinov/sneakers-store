from django.db.models import IntegerChoices


class Genders(IntegerChoices):
    MALE = 0, "male"
    FEMALE = 1, "female"
