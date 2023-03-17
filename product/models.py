from django.db import models

# Create your models here.
class category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class product(models.Model):
	img = models.ImageField(upload_to='pics', blank=True)
	cat = models.ForeignKey(category, null=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	price = models.CharField(max_length=100)
	min_order = models.CharField(max_length=100)
	material = models.CharField(max_length=100)
	filter_type = models.CharField(max_length=100)
	usage = models.CharField(max_length=100)
	brand = models.CharField(max_length=100)
	feature = models.CharField(max_length=100)
	desc = models.TextField(max_length=1000)

	def __str__(self):
		return self.name + " - " + self.cat.name