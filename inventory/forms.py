# Forms.py

from django import forms
from .models import Inventory, Supplier


class InventoryCreate(forms.ModelForm):
	class Meta:
		model = Inventory
		fields = '__all__'

class SupplierCreate(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = '__all__'