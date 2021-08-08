from django.db import models


class Category(models.Model):
    name = models.CharField(unique=True, max_length=256)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.price}'
