from rest_framework import serializers

from api.models import Category, Offer


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class OfferPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'

    def validate(self, data):
        if float(data['price']) < 0:
            raise serializers.ValidationError('The price must be greater then 0.')
        return data


class OfferGetSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Offer
        fields = '__all__'
