from django.db.models import Model, AutoField, CharField


class CoreModel(Model):
    id = AutoField(primary_key=True)
    title = CharField(max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
