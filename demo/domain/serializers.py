from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework.serializers import (
HyperlinkedModelSerializer,
HyperlinkedRelatedField,
ModelSerializer,
SerializerMethodField,
HyperlinkedIdentityField,
SlugRelatedField,
PrimaryKeyRelatedField,
)
from .models import Domain, Nameserver
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

class NameserverSerializers(ModelSerializer):
	domain = SlugRelatedField(
	queryset = Domain.objects.all(),
	slug_field='name'
	)
	class Meta:
		model = Nameserver
		fields = ['pk','name', 'domain']
		# fields = ['url','pk','name','domain', 'domain_id']

class DomainSerializers(ModelSerializer):
    nameservers = NameserverSerializers(many=True, read_only=True)
    class Meta:
        model = Domain
        fields = ['url','pk','name','nameservers']