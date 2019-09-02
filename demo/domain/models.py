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
    name = CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return URL to detail page of Domain"""
        return reverse(
            "domain_detail", kwargs={"pk": self.pk}
        )

class Nameserver(Model):
    name = CharField(max_length=40)
    domain = ForeignKey(Domain, related_name='nameservers', on_delete=CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """Return URL to detail page of Nameserver"""
        print("Models:selffffffffffffffffffff: " ,self)
        return reverse(
            "nameserver_detail", kwargs={"pk": self.pk}
        )