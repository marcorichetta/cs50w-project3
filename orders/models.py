from django.db import models

# Create your models here.

class Pasta(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Salad(models.Model):
    name = models.CharField(max_length=40)
    price = models.DecimalField(help_text="Price in U$S",max_digits=4, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - $ {self.price}"

class DinnerPlatter(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=(('S', 'Small'), ('L', 'Large')))
    price = models.DecimalField(help_text="Price in U$S", max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} - {self.get_size_display()} - $ {self.price}"

class SubExtra(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2) 

    def __str__(self):
        return f"{self.name} - $ {self.price}"

class Sub(models.Model):
    name = models.CharField(max_length=40)
    size = models.CharField(max_length=10, choices=(('S', 'Small'), ('L', 'Large')))
    price = models.DecimalField(help_text="Price in U$S", max_digits=4, decimal_places=2)
    extras = models.ManyToManyField(SubExtra, blank=True)

    def __str__(self):
        if self.extras.count() == 0:
            return f"{self.name} - {self.get_size_display()} - $ {self.price} - No Extras"
        else:
            return f"{self.name} - {self.get_size_display()} - $ {self.price} - Extras: {self.extras.in_bulk()}"

class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    style = models.CharField(max_length=10, choices=(('R', 'Regular'), ('S', 'Sicilian')))
    size = models.CharField(max_length=10, choices=(('S', 'Small'), ('L', 'Large')))
    price = models.IntegerField(help_text="Price in U$S")
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.get_style_display()} - {self.get_size_display()} - {self.price} - Toppings: {self.toppings.in_bulk()}"
