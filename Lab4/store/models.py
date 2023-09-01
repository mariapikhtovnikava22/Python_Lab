from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

class Size(models.Model):
    name = models.CharField(max_length=100)
    diameter = models.DecimalField(max_digits=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Courier:
    user = models.ForeignKey(User)

    def __str__(self):
        return f'{self.user.firstname} {self.user.lastname}'

class Client:
    phone_regex = RegexValidator(
        regex=r'^\+375 \(\d{2}\) \d{3}-\d{2}-\d{2}$',
        message="Phone number must be in the format: '+375 (29) XXX-XX-XX'")

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField(max_length=20, validators=[phone_regex], default='+375 (29) XXX-XX-XX')
    address = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.firstname} {self.user.lastname}'


class PizzaType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ForeignKey(Size, on_delete=models.PROTECT)
    image = models.ImageField()
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Order:
    pizza = models.ForeignKey(PizzaType, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    courier = models.ForeignKey(Courier, on_delete=models.PROTECT)

    def __str__(self):
        return f'Order #{self.pk}'





