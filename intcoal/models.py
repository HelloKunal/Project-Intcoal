from django.db import models

# Create your models here.
class tasks(models.Model):
	task_name = models.CharField(max_length=1000)
	
	def _str_(self):
		return self.task_name

class habits(models.Model):
	habit_name = models.CharField(max_length=1000)
	
	def _str_(self):
		return self.habit_name

class thoughts(models.Model):
	thought_name = models.CharField(max_length=1000)
	
	def _str_(self):
		return self.thought_name
