from django.db import models
from django.urls import reverse
from os import path

def product_image_upload_path(instance, filename):
    # Creates path like: products/product_name.jpg
    return path.join('products', filename)

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    image = models.ImageField(
        upload_to=product_image_upload_path,
        blank=True,
        null=True
    )
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.id})