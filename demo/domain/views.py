from django.shortcuts import render
from .models import Domain, Nameserver
from rest_framework.viewsets import ModelViewSet
from .serializers import DomainSerializer, DomainNameserverSerializers, NameserverSerializers

# Create your views here.
class DomainViewSet(ModelViewSet):
    serializer_class = DomainSerializer
    queryset = Domain.objects.all()

class NameserverViewSet(ModelViewSet):
    serializer_class = NameserverSerializers
    def get_queryset(self):
        return Nameserver.objects.filter(domain=self.kwargs['domain_pk'])