from django.db import models


class Office(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)

	def __str__(self):
		return self.name
