from django.db import models

# Create your models here.

class Axie(models.Model):
    STATUS_CHOICES = [
        ('Owned', 'Owned'),
        ('Listed', 'Listed'),
        ('Sold', 'Sold'),
    ]

    axie_id = models.CharField(max_length=50, unique=True)
    breed_count = models.IntegerField()
    axie_class = models.CharField(max_length=20)
    cards = models.TextField(help_text='Enter the cards separated by comma')
    purchase_price = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)
    sell_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Owned')

    def profit(self):
        if self.status == 'Sold':
            return self.selling_price - self.purchase_price
        return None

    def __str__(self):
        return self.axie_id

