from rest_framework import viewsets, status
from api.models import Category, Offer
from api.serializers import CategorySerializer, OfferGetSerializer, OfferPostSerializer
from rest_framework.response import Response


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data)


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all().order_by('title')
    serializer_class = OfferGetSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OfferPostSerializer
        return OfferGetSerializer

    def list(self, request, *args, **kwargs):
        offer = Offer.objects.all()
        serializer = OfferGetSerializer(offer, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.data['category'].isdigit():
            category = Category.objects.get(name=request.data['category'])
            request.data['category'] = category.id

        serializer = self.get_serializer(data=request.data)
        serializer.validate(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
