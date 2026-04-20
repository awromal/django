from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True) # Allows you to type a long description
    price = models.DecimalField(max_digits=10, decimal_places=2) # Proper format for money (e.g., 99.99)
    stock = models.IntegerField(default=0) # Tracks how many items you have left
    created_at = models.DateTimeField(auto_now_add=True) # Automatically saves when the item was added

    def __str__(self):
        return self.name # This makes the Admin panel show the product's actual name instead of "Product object (1)"