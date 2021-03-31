from django.db import models

# Create your models here.
class Intcoal(models.Model):
	title = models.CharField(max_length=1000)

	def _str_(self):
		return self.title