from django.shortcuts import render
from .models import Domain, Nameserver
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import DomainSerializers, NameserverSerializers
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
class DomainViewSet(ModelViewSet):
	queryset = Domain.objects.all()
	serializer_class = DomainSerializers

class NameserverDomainViewSet(ModelViewSet):
    queryset = Nameserver.objects.all()
    serializer_class = NameserverSerializers

    def get_queryset(self):
        try:
            return Nameserver.objects.filter(domain=self.kwargs['domain_pk'])
        except KeyError:
            return Nameserver.objects.all()