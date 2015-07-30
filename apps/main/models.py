from django.db import models
class Order(models.Model):
	name = models.TextField(max_length = 45)
	street_address = models.TextField(max_length=45)
	city = models.TextField()
	state = models.TextField(max_length = 2)
	zipcode = models.IntegerField(max_digits = 5)
	card = models.IntegerField()
	created_at = models.DateTimeField()
	class Meta:
		db_table = 'orders'

class Product(models.Model):
	order = models.ForeignKey(Order)
	item_name = models.TextField(max_length = 45)
	price = models.DecimalField(max_digits = 8, decimal_places =2)
	quantity = models.IntegerField()
	created_at = models.DateTimeField()
	class Meta:
		db_table = "products"

# Create your models here.
