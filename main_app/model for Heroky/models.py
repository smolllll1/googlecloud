from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class DishCategory(models.Model):
	title = models.CharField(max_length=50, unique=True)
	position = models.PositiveSmallIntegerField(unique=True)
	is_visible = models.BooleanField(default=True)

	def __iter__(self):
		for dishe in self.dishes.all():
			yield dishe

	def __str__(self):
		return f'{self.title}'

	class Meta:
		ordering = ('position', )


class Dish(models.Model):
	title = models.CharField(max_length=50, unique=True)
	position = models.PositiveSmallIntegerField()
	is_visible = models.BooleanField(default=True)
	category = models.ForeignKey(DishCategory, on_delete=models.CASCADE, related_name='dishes')
	is_special = models.BooleanField(default=True)
	is_signature = models.BooleanField(default=True)
	is_recomendet = models.BooleanField(default=True)
	desc = models.TextField(max_length=200, blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2)
	discount = models.DecimalField(max_digits=8, decimal_places=0)
	ingradients = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='dishes')

	def __str__(self):
		return f'{self.title}'

	def total_price(self):
		return (self.price - self.discount / 100 * self.price) * 100

	def fix_price(self):
		return self.price * 100

	class Meta:
		ordering = ('position', )

class About(models.Model):
	title = models.CharField(max_length=200, unique=True)
	body = models.TextField(max_length=4000, blank=True)
	is_visible = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.title}'

class Service(models.Model):
	service_element = [
		('M', 'clean environment'),
		('E', 'sexpert chefs'),
		('F', 'tasty food'),
	]
	is_visible = models.BooleanField(default=True)
	title = models.CharField(max_length=100, unique=True)
	body = models.TextField(max_length=4000, unique=False)
	position = models.CharField(max_length=2, choices=service_element, default='M')

	def __str__(self):
		return f'{self.title}'
	class Meta:
		ordering = ('-position', )

class Galerys(models.Model):
	photo = models.ImageField(upload_to='dishes')
	is_visible = models.BooleanField(default=True)

class Events(models.Model):
	title = models.CharField(max_length=100, unique=True)
	photo = models.ImageField(upload_to='dishes')
	is_visible = models.BooleanField(default=True)
	date = models.DateField()
	time = models.TimeField()
	message = models.TextField(max_length=1000, blank=True)

	def __str__(self):
		return f'{self.title}'

	class Meta:
		ordering = ('date', )


class Reservation(models.Model):
	phone_validator = RegexValidator(regex='^\+?3?8?0?\d{2}[ -]?(\d[ -]?){7}$',
									 message='the number should have the following format: +380xx xxx xx xx')
	email_validator = RegexValidator(regex='^\w+(_?\w*)*-?\w*(_?\w*)*@\w+(\.\w*)+$', message='xxxxxx@xxxxxx')
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, validators=(email_validator, ))
	phone = models.CharField(max_length=16, validators=(phone_validator, ))
	visit_date = models.DateField()
	visit_time = models.TimeField()
	date_request = models.DateTimeField(auto_now_add=True)
	date_response = models.DateTimeField(auto_now=True)
	quests = models.CharField(max_length=10)
	message = models.TextField(max_length=1000, blank=True)
	is_processed = models.BooleanField(default=False)

	class Meta:
		ordering = ('-date_response', )
	def __str__(self):
		return f'{self.name}\t{self.phone}\t{self.email}'
