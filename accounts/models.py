from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(default="profile1.png", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("customer", kwargs={
    #         'pk_test':self.pk_test
    #     })

class Tag(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status = models.CharField(max_length=200, blank=True, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.product.name
    