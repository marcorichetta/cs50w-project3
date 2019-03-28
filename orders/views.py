from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Pasta, Salad, DinnerPlatter, SubExtra, Sub, Topping

# Create your views here.
def index(request):


    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all()
    }

    return render(request, "orders/index.html", context)