from rest_framework_nested import routers
from .views import DomainViewSet, NameserverViewSet
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.register(r'domains', DomainViewSet)

domains_router = routers.NestedSimpleRouter(router, r'domains', lookup='domain')
domains_router.register(r'nameservers', NameserverViewSet, base_name='domain-nameservers')
# 'base_name' is optional. Needed only if the same viewset is registered more than once
# Official DRF docs on this option: http://www.django-rest-framework.org/api-guide/routers/

# urlpatterns = patterns('',
#     url(r'^', include(router.urls)),
#     url(r'^', include(domains_router.urls)),
# )

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(domains_router.urls))
]