from django.urls import path, include
from api.views import CategoryViewSet, OfferViewSet
from rest_framework import routers
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Offerable API')

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'offers', OfferViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
