from django.forms import ModelForm
from main.models import ProductEntry

class ProductEntryForm(ModelForm):
    class Meta:
        model = ProductEntry #menunjukan model yang digunakan
        fields = ["name", "price", "description", "quantity","size"]