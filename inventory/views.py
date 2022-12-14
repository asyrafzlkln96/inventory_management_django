from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import InventoryCreate, SupplierCreate
from .models import Supplier, Inventory
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def index(request):
	inventories = Inventory.objects.all()
	return render(request, "inventory/index.html", {'inventories': inventories})

def get_all_inventories(request):
	if request.method == 'GET':
		queryset = Inventory.objects.all().values()
		inventory_name = request.GET.get('name', None)
		if inventory_name is not None:
			queryset = queryset.filter(name = inventory_name).values('name', 'supplier', 'availability')
		return JsonResponse(data={'Inventory': list(queryset)}, status=status.HTTP_200_OK)


def get_inventory_by_id(request, inventory_id):
	try:
		inventory_sel = Inventory.objects.get(id = inventory_id )
	except Inventory.DoesNotExist:
		return HttpResponseNotFound('<h1>Inventory not found</h1>')
	return render(request, "inventory/inventory_detail.html", {'inventories': inventory_sel})
