from django.db.models import (
    CASCADE,
    CharField,
    DateField,
    EmailField,
    ForeignKey,
    ManyToManyField,
    Model,
    SlugField,
    TextField,
    URLField,
)

# Create your models here.
class Domain(Model):
    name = CharField(max_length=10)


class Nameserver(Model):
    name = CharField(max_length=10)
    domain = ForeignKey(Domain, related_name='domain', on_delete=CASCADE)