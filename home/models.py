from django.db import models

class Contact(models.Model):
    STATE_CHOICES = [
        ('GA', 'Goa'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('PB', 'Punjab'),
        ('RJ', 'Rajasthan'),
        ('UP', 'Uttar Pradesh'),
        ('UK', 'Uttarakhand'),
        ('WB', 'West Bengal'),
        ('DL', 'Delhi'),
    ]

    COFFEE_TYPE = [
        ('ES', 'Espresso'),
        ('LA', 'Latte'),
        ('MO', 'Mocha'),
        ('CA', 'Cappuccino'),
        ('FW', 'Flat White'),
        ('CB', 'Cold Brew'),
    ]

    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50, choices=STATE_CHOICES)
    CoffeeType = models.CharField(max_length=50, choices=COFFEE_TYPE, default='ES')
    Quantity = models.IntegerField(default=1)
    Instructions = models.TextField(max_length=100, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.Name