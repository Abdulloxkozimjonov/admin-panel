from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class Testimonials(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    img = models.ImageField(upload_to='img/photos/')
    rating = models.IntegerField()


class User(AbstractUser):
    img = models.ImageField(upload_to='foto/')
    phone_number=models.CharField(max_length=13,null=True,blank=True,validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message = 'Invalide phone number',
            code = 'Invalid number'
        )
    ])
    bio = models.CharField(max_length=13, null=True, blank=True)

    class Meta(AbstractUser.Meta):
        swappable= 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Home(models.Model):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    img = models.ImageField(upload_to='home_img/')
    email = models.ForeignKey(to='Xaridorlar', on_delete=models.PROTECT)
    address = models.CharField(max_length=55)
    date = models.DateField(auto_now=True)

class Xaridorlar(models.Model):
    ism = models.CharField(max_length=55)
    familya = models.CharField(max_length=55)
    email = models.CharField(max_length=55)
    tel_raqam = models.CharField(max_length=55)


class Sold_house(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=75, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message='Invalide email',
            code='Invalid email'
        )
    ])
    paid = models.DecimalField(max_digits=10, decimal_places=2,)
    phone = models.CharField(max_length=13, blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])