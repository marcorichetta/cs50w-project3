from django.db import models

# Create your models here.

class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Pizza(models.Model):
    tipo = models.CharField(max_length=10, choices=(('R', 'Regular'), ('S', 'Sicilian')))
    size = models.CharField(max_length=10, choices=(('S', 'Small'), ('L', 'Large')))
    precio = models.IntegerField()
    toppings = models.ManyToManyField(Topping, related_name="condimentos")
    #extras = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name="condimentos")

    def __str__(self):
        return f"{self.tipo} - {self.size} - {self.precio} - {self.toppings.name}"
