from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from orders.forms import PizzaForm
from orders.models import (DinnerPlatter, Pasta, Pizza, Salad, Sub, SubExtra,
                           Topping)


def index(request):
    """ Homepage where users can view the menu and add items to a virtual cart """
    
    form = PizzaForm()

    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Topping.objects.all(),
        "subs": Sub.objects.all(),
        "subExtras": SubExtra.objects.all(),

        "pastas": Pasta.objects.all(),
        "platters": DinnerPlatter.objects.all(),
        "salads": Salad.objects.all(),
        "form": form
    }

    return render(request, "orders/index.html", context)

@login_required(login_url='/login/')
def checkout(request):
    """ Here the """

    if request.method == 'POST':

        form = PizzaForm(request.POST)

        if form.is_valid():
            #form.save()
            messages.success(request, f'Your order was placed!')
            return redirect('index')
    else:
        return render(request, "orders/checkout.html")
