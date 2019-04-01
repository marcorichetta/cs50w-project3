from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.models import Pizza, Pasta, Salad, DinnerPlatter, SubExtra, Sub, Topping

# Create your views here.

@login_required(login_url='/login/')
def index(request):

    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all()
    }

    return render(request, "orders/index.html", context)