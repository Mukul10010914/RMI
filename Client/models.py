from django.db import models

# Create your models here.
class enquery(models.Model):
	coname = models.CharField(max_length=100)
	pname = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	number = models.CharField(max_length=100)
	desc = models.CharField(max_length=10000)

class review(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100, default=None)
	comment = models.TextField(max_length=1000, blank=True)
	rate = models.CharField(max_length=50)

	def __str__(self):
		return self.name + " - " + self.rate