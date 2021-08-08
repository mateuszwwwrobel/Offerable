from django.test import TestCase
from api.models import Category, Offer


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
