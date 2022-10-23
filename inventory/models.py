from django.db import models

# Create your models here.


class Supplier(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=100, null=False, blank=False)

	def __str__(self) -> str:
		return self.name



class Inventory(models.Model):
	id = models.AutoField(primary_key=True)
	name= models.CharField(max_length=100, null=False, blank=False)
	description = models.CharField(max_length=100, null=False, blank=False)
	note = models.TextField(null=False, blank=False)
	stock = models.IntegerField(null=False, blank=False)
	availability = models.BooleanField(null=False, blank=False)
	# supplier
	supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.name

	def get_absolute_url(self):
		return reverse('inventory-detail', args=[str(self.id)])

	def get_fields(self):
		return [(field.verbose_name, field.value_from_object(self))

				if field.verbose_name != 'supplier'
                
                else 
                    (field.verbose_name, 
                    Supplier.objects.get(pk=field.value_from_object(self)).name)
                
                for field in self.__class__._meta.fields[1:]
            ]

