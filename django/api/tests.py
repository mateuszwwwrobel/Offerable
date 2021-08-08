from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Category, Offer
from django.urls import reverse


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


# Endpoints Tests
class CategoryViewsSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.categories = []
        category_names = ['Food', 'Cars', 'Properties']
        for name in category_names:
            instance = Category.objects.create(name=name)
            cls.categories.append(instance)
        cls.category = cls.categories[0]

    def test_can_browse_all_offers(self):
        response = self.client.get(reverse("category-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.categories), len(response.data))

    def test_can_read_a_specific_offer(self):
        response = self.client.get(
            reverse("category-detail", args=[self.category.id])
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        context = {'request': None}


class OfferViewSet(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Electronics")
        cls.offer_1 = Offer.objects.create(
            title='GeForce 3080',
            price='123.99',
            description='Good graphic card.',
            category=cls.category,
        )
        offer_2 = Offer.objects.create(
            title='GeForce 3070',
            price='128.99',
            description='Good graphic card.',
            category=cls.category,
        )
        cls.offers = [cls.offer_1, offer_2]

    def test_can_browse_all_offers(self):
        response = self.client.get(reverse("offer-list"))

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(self.offers), len(response.data))

    def test_can_read_a_specific_offer(self):
        response = self.client.get(
            reverse("offer-detail", args=[self.offer_1.id])
        )
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_can_add_a_new_offer(self):
        payload = {
            "title": "GeForce 3070",
            "description": "Good graphic card",
            "price": 11.11,
            "category": 1,
        }
        before_post = Offer.objects.all().count()
        response = self.client.post(reverse("offer-list"), payload)
        after_post = Offer.objects.all().count()

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(before_post+1, after_post)

    def test_can_edit_an_offer(self):
        offer_data = {
            "title": "GeForce 3070",
            "description": "Good graphic card",
            "price": 11.11,
            "category": self.category,
        }

        offer = Offer.objects.create(**offer_data)
        payload = {
            "title": "Radeon 5700XT",
        }

        response = self.client.patch(
            reverse("offer-detail", args=[offer.id]), payload
        )

        offer.refresh_from_db()
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEqual(offer.title, payload['title'])
