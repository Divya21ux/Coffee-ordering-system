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

    PAYMENT_CHOICES = [
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
        ('paypal', 'PayPal'),
    ]

    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=15, null=True, blank=True)
    Address = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50, choices=STATE_CHOICES)
    Quantity = models.IntegerField(default=1)
    Instructions = models.TextField(max_length=100, blank=True, null=True)
    date = models.DateField()
    paymentMethod = models.CharField(max_length=20, choices=PAYMENT_CHOICES, default='credit')
    name_on_card = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiration_date = models.CharField(max_length=5, blank=True, null=True)  # "12/25"
    cvv = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return f"{self.Name} - {self.paymentMethod}"
