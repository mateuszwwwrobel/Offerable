from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api.serializers import CategorySerializer, OfferGetSerializer, OfferPostSerializer
from api.models import Category, Offer


# Models Tests
class CategoryModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        Category.objects.create(name="Vehicles")

    def test_name_max_length(self) -> None:
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 256)

    def test_string_representation_category(self) -> None:
        category = Category.objects.get(id=1)
        expected_obj_name = f'{category.name}'
        self.assertEqual(str(category), expected_obj_name)

    def test_verbose_name_plural(self) -> None:
        category = Category.objects.get(id=1)
        verbose_name_plural = category._meta.verbose_name_plural
        self.assertEqual(verbose_name_plural, 'Categories')


class OfferModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        category = Category.objects.create(name="Electronics")
        Offer.objects.create(
            title='GeForce 3080',
            price='123.99',
            description='Good graphic card.',
            category=category,
        )

    def test_title_max_length(self) -> None:
        offer = Offer.objects.get(id=1)
        max_length = offer._meta.get_field('title').max_length
        self.assertEqual(max_length, 256)

    def test_price_max_digits_and_decimal_places(self) -> None:
        offer = Offer.objects.get(id=1)
        max_digits = offer._meta.get_field('price').max_digits
        decimal_places = offer._meta.get_field('price').decimal_places
        self.assertEqual(max_digits, 8)
        self.assertEqual(decimal_places, 2)

    def test_string_representation_category(self) -> None:
        offer = Offer.objects.get(id=1)
        expected_obj_name = f'{offer.title} - {offer.price}'
        self.assertEqual(str(offer), expected_obj_name)


# Endpoints Tests - Category
class CreateCategoryTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.data = {'name': 'Food'}

    def test_can_create_new_category(self):
        response = self.client.post(reverse('category-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadCategoryTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')

    def test_can_read_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_category_detail(self):
        response = self.client.get(reverse('category-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateCategoryTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.context = {'request': None}
        self.data = CategorySerializer(self.category, context=self.context).data
        self.data.update({'name': 'Cars'})

    def test_can_updated_category(self):
        response = self.client.put(reverse('category-detail', args=[self.category.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.category.refresh_from_db()
        self.assertEqual(self.category.name, self.data['name'])


class DeleteCategoryTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')

    def test_can_delete_user(self):
        response = self.client.delete(reverse('category-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Endpoints Tests - Offer
class CreateOfferTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.offer = Offer.objects.create(
            title='GeForce 3080',
            category=self.category,
            price=123.50,
            description="Great graphic card."
        )
        self.data = {'title': 'GeForce 3070', 'category': self.category.id,
                     'price': 333.99, 'description': 'Very good graphic card.'}

    def test_can_create_new_offer(self):
        response = self.client.post(reverse('offer-list'), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadOfferTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.offer = Offer.objects.create(
            title='GeForce 3080',
            category=self.category,
            price=123.50,
            description="Great graphic card."
        )

    def test_can_read_offer_list(self):
        response = self.client.get(reverse('offer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_offer_detail(self):
        response = self.client.get(reverse('offer-detail', args=[self.category.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateOfferTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.offer = Offer.objects.create(
            title='GeForce 3080',
            category=self.category,
            price=123.50,
            description="Great graphic card."
        )

        self.context = {'request': None}
        self.data = OfferPostSerializer(self.offer, context=self.context).data
        self.data.update({'title': 'Radeon 6700'})

    def test_can_updated_offer(self):
        response = self.client.put(reverse('offer-detail', args=[self.offer.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.offer.refresh_from_db()
        self.assertEqual(self.offer.title, self.data['title'])


class DeleteOfferTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Electronics')
        self.offer = Offer.objects.create(
            title='GeForce 3080',
            category=self.category,
            price=123.50,
            description="Great graphic card."
        )

    def test_can_delete_user(self):
        response = self.client.delete(reverse('offer-detail', args=[self.offer.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
