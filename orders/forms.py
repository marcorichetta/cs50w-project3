from django.forms import ModelForm
from orders.models import Pizza

class PizzaForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'