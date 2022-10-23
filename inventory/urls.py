from django.urls import path
# from .views import index
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'inventory'

urlpatterns = [
	path("inventory", views.index, name="get_all_inventory_list"),
	path("inventory/<int:inventory_id>", views.get_inventory_by_id, name='get_inventory_by_id'),
	path("api/inventory/", views.get_all_inventories, name='get_all_inventories')
]
