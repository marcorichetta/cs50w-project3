from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from orders.models import Pizza, Pasta, Salad, DinnerPlatter, SubExtra, Sub, Topping
from orders.forms import PizzaForm

# Create your views here.

@login_required(login_url='/login/')
def index(request):

    form = PizzaForm()

    context = {
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all(),
        "form": form
    }

    return render(request, "orders/index.html", context)