from rest_framework_nested.relations import NestedHyperlinkedRelatedField
from rest_framework.serializers import (
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from .models import Domain, Nameserver
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_nested.serializers import NestedHyperlinkedModelSerializer

# class DomainSerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Domain

#     nameservers = HyperlinkedIdentityField(
#         view_name='domain-nameservers-list',
#         lookup_url_kwarg='domain_pk'
#     )

	## OR ##

    # nameservers = NestedHyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,   # Or add a queryset
    #     view_name='domain-nameservers-detail'
    #     parent_lookup_kwargs={'domain_pk': 'domain__pk'}
    # )

class NameserverSerializers(HyperlinkedModelSerializer):
	class Meta:
		model = Nameserver
		fields = ('name','domain')


class DomainNameserverSerializers(NestedHyperlinkedModelSerializer):
	parent_lookup_kwargs = {
		'domain_pk': 'domain__pk',
	}
	class Meta:
		model = Nameserver
		fields = ('url', 'name')


class DomainSerializer(HyperlinkedModelSerializer):
	class Meta:
		model = Domain
		fields = ('name', 'nameservers')

	nameservers = DomainNameserverSerializers(many=True, read_only=True)