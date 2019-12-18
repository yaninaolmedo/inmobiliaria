from django.db import models


class Estate(models.Model):
    RENTAL = 'alquiler'
    SALE = 'venta'

    TRANSACTION_TYPE = [
        (RENTAL, 'Aquiler'),
        (SALE, 'Venta'),
    ]

    transaction_type = models.CharField(
        max_length=8, choices=TRANSACTION_TYPE
    )
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    surface = models.PositiveIntegerField()
    garage = models.PositiveIntegerField()

    def __str__(self):
        return str(self.address) + ": $" + str(self.price)
